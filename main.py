from funcs import *

import mysql.connector 
import sys
import time
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=take_pass(),
    database="Moment_Book"
)

mycursor = db.cursor()

create_table = """CREATE TABLE Memories (
        Title varchar(20) NOT NULL, 
        Memory varchar(500), 
        Created datetime NOT NULL, 
        id int UNSIGNED PRIMARY KEY AUTO_INCREMENT)"""

mycursor.execute(create_table)

# insert_into = """INSERT INTO Memories (Title,Memory,Created) VALUES (%s,%s,%s)"""
# delete_row = "DELETE FROM Memories WHERE Title = '%s'"
# select_all = "SELECT * FROM Memories"
# select_memory = "SELECT Memory FROM Memories WHERE Title = '%s'"
# update_title = "UPDATE Memories SET Title='%s' WHERE id='%s'"
# update_memory = "UPDATE Memories SET Memory='%s' WHERE id='%s'"

# welcomer()

# def main():
#     opt = input('''\nHi! So what do you wanna do? :
#                     Press `c` to create a memory
#                     Press `d` to delete a memory
#                     Press `r` to read a memory
#                     Press `e` to edit a memory
#                     Press `exit` to exit the app\n : ''')

#     if opt.lower() == "c":
#         title = take_title()
#         memory = take_memory()
#         mycursor.execute(insert_into,(title,memory,datetime.now()))
#         db.commit()
#         print("New memory created !!")

#     elif opt.lower() == "d":
#         row = input("Hmm, ok give me the title of the memory you want to delete (make sure this action won't be reversed):  ")
#         confirm = input(f"Is `{row}` the memory you want to delete? ( yes/no ): ")
#         if confirm.lower() == "yes":
#             mycursor.execute(delete_row%(row,))
#             db.commit()
#             print(f"Alright! Deleted `{row}`")
#         else:
#             print("Then Enter a correct value please")

#     elif opt.lower() == "r":
#         mycursor.execute(select_all)
#         print("\nHere are all of your memories!\n")
#         for x in mycursor:
#             print(f"    -{x[0]}")
#         choose = input("Which one do you wanna read ?")
#         mycursor.execute(select_memory%(choose,))
#         for x in mycursor:
#             print("\n",x[0])
    
#     elif opt.lower() == "e":
#         mycursor.execute(select_all)
#         print("\nHere are all of your memories!\n")
#         for x in mycursor:
#             print(f"    {x[3]}. {x[0]}")
#         id = int(input("Which one do you wanna edit (1,2,3..)?: "))
#         choose= input("\nType `t` if you just wanna edit the title and `m` if the memory itself: ")
#         choose_new = input("Alright, now just give me the new content to replace! : ")
#         if choose.lower() == "t":
#             mycursor.execute(update_title%(choose_new,id))
#             db.commit()
#             print("Done!")
#         elif choose.lower() == "m":
#             mycursor.execute(update_memory%(choose_new,id))
#             db.commit()
#             print("Done!")
            
#     elif opt.lower() == "exit":
#         sys.exit()

#     else:
#         print("please enter a correct value")

# while True:
#     main()
#     time.sleep(2)