from flask import Blueprint, render_template, request, flash
#from flask_login import login_required,  current_user
#from .models import Note
#from .import db
#import json

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
  return render_template("login.html")

@auth.route('/logout')
def logout():
  return render_template("home.html")

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    email = request.form.get('email')
    firstname = request.form.get('firstName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    if len(email) < 4:
      flash('Email must be greater than 3 characters.',category='error')
    elif len(firstname) < 2:
      flash('First name must be greater than 1 character.',category='error')
    elif password1 != password2:
      flash('Passwords do not match.',category='error')
    elif len(password1) < 7:
      flash('Password must be greater than 6 characters.',category='error')
    else:
      flash('Welcome '+firstname, category='success')
    
  
    
    
  return render_template("signin.html")