from app import app, db
from flask import render_template, redirect, request, flash, url_for
from models import LostProp
from forms import LostReport

from flask_login import login_required, logout_user

#login manager module for flask login
#@login_manager.user_loader
#def load_user(userid):
#    return User.query.get(userid)

#index page
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/lost_report', methods=["GET", "POST"])
def lost_report():
    form = LostReport()
    if form.validate_on_submit():
        lost_item = LostProp(description = form.description.data,first_name = form.first_name.data, last_name = form.last_name.data, telephone = form.last_name.data, address = form.finderAddress.data, email = form.finderEmail.data, loser_postcode = form.finderPostcode.data, type = form.itemType.data, colour = form.itemColour.data, street = form.streetFound.data, borough = form.borough.data, postcode = form.postcode.data)
        db.session.add(lost_item)
        db.session.commit()

    return render_template("lost_report.html", form=form)