from flask_login import UserMixin
from app import db
# from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    #insta_account = relationship("InstagramAccount", back_populates="user")


#class InstagramAccount(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    user_id = db.Column(Integer, ForeignKey('user.id'))
#    instagram_username = db.Column(db.String(500))
#    instagram_password = db.Column(db.String(500))


#class InstagramConfigs(db.Model):
#    pass


