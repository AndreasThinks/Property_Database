from app import app, db
from flask import render_template, redirect, request, flash, url_for
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


@app.route('/lost_report')
def lost_report():
    form = LostReport()
    return render_template("lost_report.html", form=form)