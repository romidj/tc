from market import app
from flask import render_template
from market.models import Post
@app.route('/')
@app.route('/home')
def home_page():
    return "<h1>never mind <h1>"

