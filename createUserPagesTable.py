import mysql.connector
import mysql
from mysql.connector import errorcode

cnx = mysql.connector.connect(user='osadmin', password='mhacksfive', host='openspace.c8mvjcla3p7q.us-west-2.rds.amazonaws.com', database='openspace')
cursor = cnx.cursor()

# createTemplatesTable = (
#     "CREATE TABLE templates ("
#     "  template_id INT NOT NULL PRIMARY KEY,"
#     "  template_content text NOT NULL"
#     ") ENGINE=InnoDB")

# createPagesTable = (
#    "CREATE TABLE pages ("
#    "  page_id INT NOT NULL PRIMARY KEY,"
#    "  user_id INT NOT NULL REFERENCES users,"
#    "  template_id INT NOT NULL REFERENCES templates"
#    ") ENGINE=InnoDB")

# createVariablesTable = (
#     "CREATE TABLE template_variables ("
#     "  template_id INT NOT NULL AUTO_INCREMENT REFERENCES templates,"
#     "  var_name VARCHAR(255) NOT NULL,"
#     "  var_content VARCHAR(255) NOT NULL,"
#     "  PRIMARY KEY(template_id, var_name, var_content)"
#     ") ENGINE=InnoDB")

# cursor.execute(createTemplatesTable)
# cursor.execute(createPagesTable)
# cursor.execute(createVariablesTable)

# template = """
#    Hello, {{ name }}! This is my basic template. Let's see the page title, its {{ title }}. How Fascinating! Fuck this shit, {{ variableName }}. 
# """

# query = ("INSERT INTO templates (template_id, template_content, template_name, author_id) VALUES (%s, %s, %s, %s)")
# values = (1, template, 'Cool Template', 1)
# cursor.execute(query, values)
# cnx.commit()

# query = ("INSERT INTO pages (page_id, user_id, template_id) VALUES (%s, %s, %s)")
# values = (1, 1, 1)
# cursor.execute(query, values)
# cnx.commit()
query = ("SELECT template_name FROM templates")
# query = ("ALTER TABLE templates ORDER BY template_id, template_name, template_html, template_css, template_js, author_id")
cursor.execute(query)
# cnx.commit()
row = cursor.fetchall()
print row

cursor.close()
cnx.close()