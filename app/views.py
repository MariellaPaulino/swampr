# -*- coding: utf-8 -*-

from app import app, db
from flask import render_template
from models import Post, User

@app.route('/')
def index(): 
	users = User.query.all()
	posts= Post.query.all()
	return render_template ("index.html", users=users, posts=posts)
