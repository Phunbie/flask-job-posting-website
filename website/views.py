from flask import Blueprint, render_template, request
#from flask_login import login_required,  current_user
#from .models import Note
#from .import db
#import json

views = Blueprint('views', __name__)

@views.route('/home')
@views.route('/')
def home():
  return render_template("home.html")

@views.route('/more')
def moreJobs():
  return render_template("More-jobs.html")

@views.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
  data = request.form
  return render_template("dashboard.html")