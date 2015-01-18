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
#     "CREATE TABLE variables ("
#     "  page_id INT NOT NULL REFERENCES pages,"
#     "  var_name VARCHAR(255) NOT NULL,"
#     "  var_content VARCHAR(255) NOT NULL,"
#     "  PRIMARY KEY(page_id, var_name, var_content)"
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

query = ("SELECT * FROM pages")
cursor.execute(query)
row = cursor.fetchall()
print row

cursor.close()
cnx.close()