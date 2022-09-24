from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Jobs(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  company = db.Column(db.String(50))
  job = db.Column(db.String(150))
  location = db.Column(db.String(150))
  details = db.Column(db.String(1000))
  date = db.Column(db.DateTime(timezone=True), default = func.now())
  employer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  userlist = db.relationship('User')
  
class User(db.Model,UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(50), unique=True)
  password = db.Column(db.String(150))
  firstname = db.Column(db.String(150))
  joblist = db.relationship('Jobs')
  jobid_id = db.Column(db.Integer, db.ForeignKey('jobs.id'))