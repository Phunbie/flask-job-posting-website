from flask import Blueprint, render_template
#from flask_login import login_required,  current_user
#from .models import Note
#from .import db
#import json

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
  return render_template("login.html")

@auth.route('/logout')
def logout():
  return render_template("home.html")

@auth.route('/signup')
def signup():
  return render_template("signin.html")