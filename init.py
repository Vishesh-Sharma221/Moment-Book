from funcs import *

import mysql.connector 
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=take_pass(),
    database="Moment_Book"
)

mycursor = db.cursor()

mycursor.execute("SELECT * from VAYS")

for x in mycursor:
    print(x)

