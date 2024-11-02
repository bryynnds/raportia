from app import db
from datetime import datetime

class User(db.Model):
  id=db.Column(db.BigInteger, primary_key=True, autoincrement=True)
  name=db.Column(db.String(250), nullable=False)
  email=db.Column(db.String(50), index=True, unique=True, nullable=False)
  password=db.Column(db.String(250), nullable=False)
  
  def __repr__(self):
    return '<user {}>'.format(self.name)