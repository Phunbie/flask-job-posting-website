from flask import Blueprint, render_template
#from flask_login import login_required,  current_user
#from .models import Note
#from .import db
#import json

views = Blueprint('views', __name__)


@views.route('/')
def home():
  return render_template("base.html")

@views.route('/more')
def moreJobs():
  return render_template("base.html")

@views.route('/dashboard')
def dashboard():
  return render_template("dashboard.html")