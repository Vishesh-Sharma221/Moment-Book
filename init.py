import mysql.connector 

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="visheshsharma22",
    database="Moment_Book"
)

mycursor = db.cursor()

# mycursor.execute("CREATE TABLE test (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
# mycursor.execute("INSERT INTO test (name,age) VALUES(%s,%s)", ("Joe","19"))
mycursor.execute("SELECT * FROM test")
# db.commit()
for x in mycursor:
    print(x)