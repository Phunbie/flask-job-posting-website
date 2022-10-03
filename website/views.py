from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_required,  current_user
from .models import Jobs
from .import db
from .models import User
#import json
views = Blueprint('views', __name__)

@views.route('/home')
@views.route('/')
def home():
  job=Jobs.query.all()
  job2=[]
  for j in job:
      job2.append(j)
  job2=job2[::-1]
  job2=job2[:4]
  return render_template("home.html", user=current_user, job=job,job2=job2)

@views.route('/more')
def moreJobs():
  job=Jobs.query.all()
  job1=[]
  for j in job:
    job1.append(j)
  job1=job1[::-1]
  return render_template("More-jobs.html", user=current_user, job=job, job1=job1)

@views.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
  if request.method == 'POST':
    company = request.form.get('company')
    email = request.form.get('email')
    job = request.form.get('job')
    location = request.form.get('location')
    details = request.form.get('details')
    if len(company) < 3:
      flash('Company name must be greater than 2 characters.',category='error')
    elif len(job) < 3:
      flash('Job position must be greater than 2 characters.',category='error')
    elif len(email) < 3:
      flash('email must be greater than 2 characters.',category='error')
    elif len(location) < 3:
      flash('Location must be greater than 2 characters.',category='error')
    elif len(details) < 3:
      flash('Location must be greater than 2 characters.',category='error')
    else:
      new_job = Jobs(company=company, email=email, job=job, location=location, details=details, employer_id=current_user.id)
      db.session.add(new_job)
      db.session.commit()
      flash('New job added!', category='success')
      
  return render_template("dashboard.html", user=current_user)


@views.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    task_to_delete = Jobs.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        flash('Job deleted!', category='success')
        return redirect("/dashboard")
    except:
        return 'There was a problem deleting that task'
  