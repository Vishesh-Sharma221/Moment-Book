import mysql.connector 
from MomentBook.queries import *
#  THIS IS WHERE ALL THE ESSENTIAL FUNCTIONS AND VARIABLES ARE STORED

def connect_to_server():
	username = input("Please enter your MySql server username: ")
	password = input(f"Please enter the password for {username}: ")

	try:
		db = mysql.connector.connect(
			host="localhost",
			user=username,
			passwd=password,
			auth_plugin = "mysql_native_password"
		)		
		return db 
	except mysql.connector.errors.ProgrammingError:
		print("Incorrect username/password, please try again!")
		return connect_to_server()

def connect_cursor(database):
	if database.is_connected():
		print(f"\n Logged in Successfully! ")
	else:
		print("Couldn't log in to the server! Please try again.")
		return 
	return database.cursor()
		



def welcomer():
	print("\n----------------WELCOME TO MOMENT BOOK---------------- ")
	print("\nfeel free to tell me all of your stories and moments :D")



