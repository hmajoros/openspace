from flask import render_template, Blueprint, g, session, request, redirect, url_for
from flask.ext.login import current_user, login_required

import os
import mysql.connector
import mysql


upload = Blueprint('upload', __name__, url_prefix='/upload')

@upload.before_request
def before_request():
    g.user = current_user

@upload.route('/')
@login_required
def index():
    return render_template('upload.html', title='Upload', user=current_user)

@upload.route('/template', methods=['GET', 'POST'])
def template():
    if request.method == 'POST':
        db_user = os.environ['DB_USER']
        db_pass = os.environ['DB_PASSWORD']
        db_host = os.environ['DB_HOST']
        db_name = os.environ['DB_NAME']

        conn = mysql.connector.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
        cursor = conn.cursor()

        query = ("INSERT INTO templates (template_content, template_name, author_id) VALUES (%s, %s, %s)")
        values = (request.form['content'], request.form['template_name'], current_user.get_id())
        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for('home.index'))
    return redirect(url_for('upload.index'))
