import mysql.connector
import mysql
from mysql.connector import errorcode

DB_NAME = 'openspace'

createTable = (
    "CREATE TABLE `userPages` ("
    "  `page_id` INT NOT NULL,"
    "  `user_id` INT NOT NULL,"
    "  `page_template` text NOT NULL,"
    "  `page_content` text NOT NULL,"
    "  PRIMARY KEY (`page_id`)"
    ") ENGINE=InnoDB")

cnx = mysql.connector.connect(user='osadmin', password='mhacksfive', host='openspace.c8mvjcla3p7q.us-west-2.rds.amazonaws.com', database='openspace')
cursor = cnx.cursor()

cursor.execute(createTable)