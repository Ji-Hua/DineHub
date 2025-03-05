from flask import Blueprint, render_template, request, redirect, url_for
from DineHub import db
from DineHub.models import DinnerProposal
from datetime import datetime

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return render_template("index.html")

@main_bp.route("/propose", methods=["GET", "POST"])
def propose_dinner():
    if request.method == "POST":
        proposer = "A"  # Hardcoded for now, replace with user authentication later
        invited_user = "B"  # Hardcoded for now
        selected_date = request.form.get("date")

        # Check if a proposal already exists for this date
        existing_proposal = DinnerProposal.query.filter_by(owner=proposer, date=selected_date).first()
        if existing_proposal:
            return redirect(url_for("main.view_proposal", proposal_id=existing_proposal.id))

        new_proposal = DinnerProposal(owner=proposer, invited_user=invited_user, date=selected_date)
        db.session.add(new_proposal)
        db.session.commit()

        return redirect(url_for("main.view_proposal", proposal_id=new_proposal.id))

    return render_template("propose.html")


@main_bp.route("/history")
def dinner_history():
    proposals = DinnerProposal.query.all()
    return render_template("history.html", proposals=proposals)


@main_bp.route("/proposal/<int:proposal_id>", methods=["GET", "POST"])
def view_proposal(proposal_id):
    proposal = DinnerProposal.query.get_or_404(proposal_id)
    user = "A"  # Hardcoded for now, replace with authentication later

    if request.method == "POST":
        action = request.form.get("action")
        dish = request.form.get("dish")

        if action == "add_a":
            proposal.a_proposed = f"{proposal.a_proposed},{dish}" if proposal.a_proposed else dish
        elif action == "add_b":
            proposal.b_proposed = f"{proposal.b_proposed},{dish}" if proposal.b_proposed else dish
        elif action == "finalize":
            proposal.final_decision = ",".join(request.form.getlist("final_dishes"))
            proposal.status = "finalized"

        db.session.commit()
        return redirect(url_for("main.view_proposal", proposal_id=proposal.id))

    return render_template("proposal.html", proposal=proposal, user=user)
