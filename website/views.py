from flask import Blueprint, render_template, request, flash
from flask_login import login_required,  current_user
from .models import Jobs
from .import db
#import json

views = Blueprint('views', __name__)

@views.route('/home')
@views.route('/')
def home():
  return render_template("home.html",user=current_user)

@views.route('/more')
def moreJobs():
  return render_template("More-jobs.html", user=current_user)

@views.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
  if request.method == 'POST':
    company = request.form.get('company')
    job = request.form.get('job')
    location = request.form.get('location')
    details = request.form.get('details')
    if len(company) < 3:
      flash('Company name must be greater than 2 characters.',category='error')
    elif len(job) < 3:
      flash('Job position must be greater than 2 characters.',category='error')
    elif len(location) < 3:
      flash('Location must be greater than 2 characters.',category='error')
    elif len(details) < 3:
      flash('Location must be greater than 2 characters.',category='error')
    else:
      new_job = Jobs(company=company, job=job, location=location, details=details)
      db.session.add(new_job)
      db.session.commit()
      flash('New job added!', category='success')
      
  return render_template("dashboard.html", user=current_user)