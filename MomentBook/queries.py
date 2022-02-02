# ALL THE QUERIES FOR MOMENT BOOK ARE HERE 

# ----- to edit the table

insert_into = """INSERT INTO Memories (Title,Memory,Created) VALUES (%s,%s,%s)"""
delete_row = "DELETE FROM Memories WHERE Title = '%s'"
select_all = "SELECT * FROM Memories"
select_memory = "SELECT Memory FROM Memories WHERE Title = '%s'"
select_title = "SELECT Title,Created,id FROM Memories"
update_title = "UPDATE Memories SET Title='%s' WHERE id='%s'"
update_memory = "UPDATE Memories SET Memory='%s' WHERE id='%s'"

# ----- to create the basic table and database

create_table = """CREATE TABLE IF NOT EXISTS Memories (
        Title varchar(20) NOT NULL, 
        Memory varchar(500), 
        Created datetime NOT NULL, 
        id int UNSIGNED PRIMARY KEY AUTO_INCREMENT)"""

create_database = "CREATE DATABASE IF NOT EXISTS Moment_Book"
use_database = "USE Moment_Book"