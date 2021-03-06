from flask import render_template, Blueprint, g, session, redirect, url_for, request
from flask.ext.login import current_user, login_required

import os
import mysql.connector

editor = Blueprint('editor', __name__, url_prefix='/editor')

@editor.before_request
def before_request():
    g.user = current_user

@editor.route('/')
@login_required
def index():
    pages = getPages()
    if request.args.get('page_id') is not None:
        db_user = os.environ['DB_USER']
        db_pass = os.environ['DB_PASSWORD']
        db_host = os.environ['DB_HOST']
        db_name = os.environ['DB_NAME']

        conn = mysql.connector.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
        cursor = conn.cursor()
        query = ("SELECT t.template_html, t.template_css, t.template_js "
                 "FROM templates t, pages p "
                 "WHERE page_id = %(page_id)s "
                 "AND p.template_id = t.template_id")
        
        cursor.execute(query, { 'page_id' : request.args.get('page_id') })
        row = cursor.fetchone()

        html = row[0]
        css = row[1]
        js = row[2]
        return render_template('editor.html', 
                                title='Editor', 
                                user=current_user, 
                                pages=pages, 
                                edit=True,
                                html=html, css=css, js=js)
    return render_template('editor.html', title='Editor', user=current_user, pages=pages, edit=False)


@editor.route('/save', methods=['GET', 'POST'])
@login_required
def save():
    if request.method == 'POST':
        db_user = os.environ['DB_USER']
        db_pass = os.environ['DB_PASSWORD']
        db_host = os.environ['DB_HOST']
        db_name = os.environ['DB_NAME']

        conn = mysql.connector.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
        cursor = conn.cursor()
        # query1 = ("SELECT ")


        query1 = ("UPDATE pages"
                  "SET template_html = %(html)s, template_css = %(css)s, template_js = %(js)s "
                  "WHERE page_id = %(page_id)s")

        cursor.execute(query, { 'html' : request.form['html'], 'css' : request.form['css'], 
                                'js' : request.form['js'], 'page_id' : request.form['page_id'] })
        conn.commit()

        cursor.close()
        conn.close()
        return redirect(url_for('editor.index'))
    return redirect(url_for('home.index'))



def getPages():
    db_user = os.environ['DB_USER']
    db_pass = os.environ['DB_PASSWORD']
    db_host = os.environ['DB_HOST']
    db_name = os.environ['DB_NAME']

    conn = mysql.connector.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
    cursor = conn.cursor()
    query = ("SELECT page_id, page_name FROM pages WHERE user_id = %(user_id)s")
    
    cursor.execute(query, { 'user_id' : current_user.get_id() })
    
    pages = []

    row = cursor.fetchone()
    while row is not None:
        page = Page(row[0], row[1])
        pages.append(page)
        row = cursor.fetchone()
    return pages


class Page(object):
    page_id = 0
    page_name = ""

    def __init__(self, page_id, page_name):
        self.page_id = page_id
        self.page_name = page_name


