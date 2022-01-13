
#  MAIN FILE ------

from initials import *

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

welcomer()

def main():
    opt = input('''\n                   ~ MENU ~ 

Select an action you want to perform:

        1.  Press `c` to create a memory
        2.  Press `d` to delete an existing memory
        3.  Press `v` to view all the memories created
        4.  Press `e` to edit a memory
        5.  Press `exit` to exit the app\n : ''')

    if opt.lower() == "c":
        title = take_title()
        memory = take_memory()
        mycursor.execute(insert_into,(title,memory,datetime.now()))
        db.commit()
        print("New memory created !!")

    elif opt.lower() == "d":
        row = input("Hmm, ok give me the title of the memory you want to delete (make sure this action won't be reversed):  ")
        confirm = input(f"Is `{row}` the memory you want to delete? ( yes/no ): ")
        if confirm.lower() == "yes":
            mycursor.execute(delete_row%(row,))
            db.commit()
            print(f"Alright! Deleted `{row}`")
        else:
            print("Then Enter a correct value please")

    elif opt.lower() == "v":
        mycursor.execute(select_all)
        print("\nHere are all of your memories!\n")
        for x in mycursor:
            print(f"    --> {x[0]} on {x[2]}")
        choose = input("Which one do you wanna read ?")
        mycursor.execute(select_memory%(choose,))
        for x in mycursor:
            print("\n",x[0])
    
    elif opt.lower() == "e":
        mycursor.execute(select_all)
        print("\nHere are all of your memories!\n")
        
        for x in mycursor:
            print(f"    {x[3]}. {x[0]}  on {x[2]}")

        id = int(input("\nWhich one do you wanna edit (1,2,3..)?: "))
        choose= input("\nType `t` if you just wanna edit the title and `m` if the memory itself: ")
        choose_new = input("\nAlright, now just give me the new content to replace! : ")

        if choose.lower() == "t":
            mycursor.execute(update_title%(choose_new,id))
            db.commit()
            print("Done!")

        elif choose.lower() == "m":
            mycursor.execute(update_memory%(choose_new,id))
            db.commit()
            print("Done!")
            
    elif opt.lower() == "exit":
        sys.exit()

    else:
        print("please enter a correct value")

while True:
    main()
    time.sleep(5)