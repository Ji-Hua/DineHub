This website should have the following function: 
1. any user (my wife or me) could post a dinner proposal (eat at home or a certain restaurant), and it will be visible to all the other users; 
2. if the proposal is dine-out, the proposer could give a list of choice (name of restaurants), and all the users (include the proposer could make a ranked vote) and the choices will be ranked by weighted votes;
    2.1 we could list the yelp/opentable/google review of the restaurant, and also reservation availability
3. if the proposal is eat at home, the proposer should be able to list a collection of dishes for the dinner, and this list can be modified by other users to propose a replacement or add/remove a dish, etc.
    3.1. any user could post a recipe for a given dish;
4. It should have a calendar of what we had for each day.

5. fridge management, scan supermarket receipt
The programming language should be Python.
Let's start this

This is not exactly what I want to have. Let's refactor it.
Let's assume there are two users A and B. 
0. A should own the proposal and hence A should have the final decision
1. in the dinner proposal page, it should have a drop down menu for selecting date, so that the user A could propose for a certain date.
  1.1 by default it will be today
2. after the user selected the date, then A could submit proposals by input text then click `add` button, it should add the dish. Then the dish will be displayed as a card under a `A-proposed` tab.
3. Other user, B, should see the same thing as A. He could click the dish card A proposed, and it will show under his tab `B-proposed`, meaning B wants this dish as well.
  3.1 B could propose other dishes as well, like what A did. it will show up in B's tab. 
4. A could review both what A and B propsed and make a final decision. the final decision will show under `final decision`.

So in general, one user (in this case will be A) could start a discussion and he owns the final right to make decision. He could invite other users (aka B) into this discussion, and they could change their proposal. the proposal will display under each user's tab. Then there is a final decision tab