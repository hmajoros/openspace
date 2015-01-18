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

query = ("SHOW TABLES")
cursor.execute(query)
print cursor.fetchall()

cursor.close()
cnx.close()