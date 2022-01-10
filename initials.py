
#  THIS IS WHERE ALL THE ESSENTIAL FUNCTIONS AND VARIABLES ARE STORED

insert_into = """INSERT INTO Memories (Title,Memory,Created) VALUES (%s,%s,%s)"""
delete_row = "DELETE FROM Memories WHERE Title = '%s'"
select_all = "SELECT * FROM Memories"
select_memory = "SELECT Memory FROM Memories WHERE Title = '%s'"
update_title = "UPDATE Memories SET Title='%s' WHERE id='%s'"
update_memory = "UPDATE Memories SET Memory='%s' WHERE id='%s'"

def take_pass():
	pwd = input("\nPlease enter your password to continue: \n")
	return pwd

def take_title():
	title = input("\nHey, What should be the title of this memory saved as? \n")
	return title

def take_memory():
	mem = input("\nAlright! Now tell me all about it, we'll keep it a secret haha \n")
	return mem

def welcomer():
	print("\n----------------MOMENT BOOK---------------- \n")
	print("\nWelcome! feel free to tell me all of your stories and moments \n")

