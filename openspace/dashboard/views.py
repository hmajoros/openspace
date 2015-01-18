from flask import render_template, Blueprint, g, session, redirect, url_for, request
from flask.ext.login import current_user

import os
import mysql.connector

dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard.before_request
def before_request():
    g.user = current_user

@dashboard.route('/')
def index():
    sites = getSitesFor(current_user.get_id())
    return render_template('dashboard.html', 
                            title='Dashboard', 
                            user=current_user, 
                            sites=sites)

@dashboard.route('/create_page', methods=['GET', 'POST'])
def create_page():
    if request.method == 'POST':
        db_user = os.environ['DB_USER']
        db_pass = os.environ['DB_PASSWORD']
        db_host = os.environ['DB_HOST']
        db_name = os.environ['DB_NAME']

        conn = mysql.connector.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
        cursor = conn.cursor()
        query = ("INSERT INTO pages (user_id, template_id, page_name) VALUES (%s, %s, %s)")
        values = (current_user.get_id(), request.form['template_id'], request.form['page_name'])

        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for('dashboard.index'))
    return redirect(url_for('home.index'))




def getSitesFor(user_id):
    db_user = os.environ['DB_USER']
    db_pass = os.environ['DB_PASSWORD']
    db_host = os.environ['DB_HOST']
    db_name = os.environ['DB_NAME']

    conn = mysql.connector.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
    cursor = conn.cursor()
    query = ("SELECT t.template_name, p.page_name FROM templates t, pages p, users u "
             "WHERE u.user_id = %(user_id)s "
             "AND u.user_id = p.user_id "
             "AND p.template_id = t.template_id")

    cursor.execute(query, { 'user_id' : user_id })
    
    sites = []

    row = cursor.fetchone()
    while row is not None:
        site = Site(row[0], row[1])
        sites.append(site)
        row = cursor.fetchone()
    return sites

class Site(object):
    t_name = ""
    p_name = ""
    
    def __init__(self, t_name, p_name):
        self.t_name = t_name
        self.p_name = p_name


