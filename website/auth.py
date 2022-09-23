from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from .import db
#import json

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
  if request.method== 'POST':
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
      if check_password_hash(user.password, password):
        flash('Logged in sucessfully!', category='success')
        login_user(user, remember=True)
        return redirect(url_for('views.dashboard'))
      else:
        flash('Incorrect password, try again.', category='error')
    else:
      flash('Email does not exist.', category='error')
      
    
  return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('views.home'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    email = request.form.get('email')
    firstname = request.form.get('firstName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    
    user = User.query.filter_by(email=email).first()
    if user:
      flash('Email already exists.', category='error')
    elif len(email) < 4:
      flash('Email must be greater than 3 characters.',category='error')
    elif len(firstname) < 2:
      flash('First name must be greater than 1 character.',category='error')
    elif password1 != password2:
      flash('Passwords do not match.',category='error')
    elif len(password1) < 7:
      flash('Password must be greater than 6 characters.',category='error')
    else:
      new_user = User(email=email, firstname=firstname, password=generate_password_hash(password1, method='sha256'))
      db.session.add(new_user)
      db.session.commit()
      flash('Welcome '+firstname, category='success')
      login_user(user, remember=True)
      return redirect(url_for('views.dashboard'))
  
    
    
  return render_template("signin.html")