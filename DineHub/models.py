from datetime import datetime
from . import db

class DinnerProposal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id", name="fk_owner_id"), nullable=False)  # Add explicit name
    invited_user = db.Column(db.String(100), nullable=False)  # Username of invited user (B)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    a_proposed = db.Column(db.Text, nullable=True)
    b_proposed = db.Column(db.Text, nullable=True)
    final_decision = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), default="pending")

    def __repr__(self):
        return f"<DinnerProposal {self.id} - {self.date} - {self.status}>"



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    proposals = db.relationship("DinnerProposal", backref="owner_ref", lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"
