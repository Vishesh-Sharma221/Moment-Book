
#  MAIN FILE IMPORTS 

from database_funcs import *
from queries import * 
from datetime import datetime
from tabulate import tabulate 
import sys

if __name__ == "__main__":
    db = connect_to_server() #connects user to the server

    mycursor = connect_cursor(db) #connects cursor which we use to execute commands in sql with python

# executing the queries for basic requirements in our database 
    mycursor.execute(create_database)
    mycursor.execute(use_database)
    mycursor.execute(create_table) 

    welcomer()

    def menu():
        print('''\n                   ~ MENU ~ 

        These are the commands you can perform :

            1.  Create
            2.  Edit
            3.  View
            4.  Delete
            5.  Type `exit` to exit the app or 'menu' to see these commands again ''')

# this class will contains all the methods to get input from the user 
class Inputs():
    def __init__(self):
        pass
    def take_pass():
        pwd = input("\nPlease enter your password to continue: \n")
        return pwd

    def take_user():
        pwd = input("\nPlease enter your username: \n")
        return pwd	

    def take_title():
        title = input("\nHey, What should be the title of this memory saved as? \n")
        return title

    def take_memory():
        mem = input("\nAlright! Now tell me all about it, we'll keep it a secret haha \n")
        return mem

# this class will contain all the methods used to perform cred functions 
# CRED - (create,read,edit,delete)
class Cred():
    def __init__(self):
        pass

    def create(title,memory,cursor,database):
        cursor.execute(insert_into,(title,memory,datetime.now()))
        database.commit()
        print('New memory created!')

    def edit(cursor,db):
        cursor.execute(select_all)
        result = cursor.fetchall()

        print("\nHere are all of your memories!\n")
        print(tabulate(result,headers=['Title','Memory','Created','ID'], tablefmt='fancy_grid'))

        id = int(input("\nWhich one do you wanna edit (1,2,3..)?: "))
        choose= input("\nType `t` if you just wanna edit the title and `m` if the memory itself: ")
        choose_new = input("\nAlright, now just give me the new content to replace! : ")

        if choose.lower() == "t":
            cursor.execute(update_title%(choose_new,id))
            db.commit()
            print("Done!")

        elif choose.lower() == "m":
            cursor.execute(update_memory%(choose_new,id))
            db.commit()
            print("Done!")

    def view(cursor):
        cursor.execute(select_title)
        result = cursor.fetchall()
        print("\nHere are all of your memories!\n")
        print(tabulate(result,headers=['Title','Created','id'], tablefmt='fancy_grid'))
        mem = input("\nWhich memory you want to see? ")
        query = select_memory%(mem,)
        cursor.execute(query)
        res = cursor.fetchall()
        print("\n",tabulate(res, tablefmt='fancy_grid'))

    def delete(cursor,db):
        cursor.execute(select_all)
        result = cursor.fetchall()
        print(tabulate(result,headers=['Title','Memory','Created','ID'], tablefmt='fancy_grid'))
        row = input("Hmm, ok give me the title of the memory you want to delete (make sure this action won't be reversed):  ")
        confirm = input(f"Is `{row}` the memory you want to delete? ( yes/no ): ")
        if confirm.lower() == "yes":
            cursor.execute(delete_row%(row,))
            db.commit()
            print(f"Alright! Deleted `{row}`")

# just a function to check the command user gave as an input
def check(opt,cursor,db):
    if opt.lower() == "create" or opt.lower() == "1":
        Cred.create(Inputs.take_title(),Inputs.take_memory(),cursor,db)

    elif opt.lower() == "edit" or opt.lower() == "2":
        Cred.edit(cursor,db)

    elif opt.lower() == "view" or opt.lower() == "3":
        Cred.view(cursor)

    elif opt.lower() == "delete" or opt.lower() == "2":
        Cred.delete(cursor,db)

    elif opt.lower() == "menu":
        menu()
    
    elif opt.lower() == "exit":
        sys.exit()

    else:
        print("please enter a correct value")

# the main loop we will be running infinitely 
def main():
    running = True
    try:
        while running:
            global opt 
            opt = input("\nCommand: ")

            check(opt,mycursor,db)
    except mysql.connector.errors.DataError:
        print("\nData too long! Enter a shorter value please")
        main()
menu()   
main()