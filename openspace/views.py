from flask import render_template
from openspace import app
import os
import mysql.connector

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
