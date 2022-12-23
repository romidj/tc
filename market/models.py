from flask import Flask, render_template, request, session
from market import db

class Post(db.Model):
    post_id = db.Column(db.Integer() , primary_key=True)
    mark = db.Column(db.String(length=255), nullable=False , unique=True)
    price = db.Column(db.Integer() ,nullable=False)
    kelometrage = db.Column(db.Integer() ,nullable=False)
 

class User(db.Model):
    userId = db.Column(db.Integer() , primary_key=True)
    username = db.Column(db.String(length=255), nullable=False  )
    email = db.Column(db.String(length=255), nullable=False , unique=True) 
    password = db.Column(db.String(255) , unique = True)

class wish_list (db.Model):
         userID =  db.Column(db.Integer() ,primary_key=True)
         Username =  db.Column(db.String(length=255), nullable=False  )
         post_id = db.Column(db.Integer() ,nullable=False)
