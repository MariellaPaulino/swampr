# -*- coding: utf-8 -*-

from app import app
from flask import render_template
from models import Post

@app.route('/')
def index(): 
	some_post = Post ("not much to say", "Aliya", "Today was 			uneventful.")
	some_other_post = Post ("alot happened today", "Aliya", "a lot 			happened today.")
	return render_template ("index.html", posts=[some_post, some_other_post])
