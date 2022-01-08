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
welcomer()
title = take_title()
memory = take_memory()

Q1 = "CREATE TABLE Memories (Title varchar(20) NOT NULL, Memory varchar(500), Created datetime NOT NULL, id int PRIMARY KEY AUTO_INCREMENT UNSIGNED)"

Q2 = "INSERT INTO Memories (Title,Memory,Created) VALUES (%s,%s,%s)"

mycursor.execute(Q2,(title,memory,datetime.now()), multi = True)
db.commit()