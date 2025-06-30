# DB operations
# Establish the connection  > ID
# create the file - > creating the database
# Open the file -> entering to db
# Write/read -> cursor operation / execute > Instance ID
#     creat the table
#     from our application
#     setting to which row, clmn etc..
#     retrive 
#     fetching
#     sorting, filtering

#     CRUD - > add, read, find,delete

# if write save the file -> commit the query
# close the file -> close the db

import mysql.connector as db

#Connecting to the server 
conn = db.connect(
    
    host = "localhost",
    user = "root",
    password = "",
    port = 3306
    
)
print("connected successfuly")

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS pythonDB") #create DB
print("Database created")
conn.database="pythonDB"    #connecting DB
print("connected to the DB")
# Create Table
cursor.execute("CREATE TABLE IF NOT EXISTS users(id INT PRIMARY KEY, name VARCHAR(20), email VARCHAR(50))")
print("Table created")
# Add Data to the TABLE
cursor.execute("INSERT INTO users (id , name, email) VALUES (%s,%s,%s)",("3","Rajesh","sample@gmail.com"))
print("Data added")
conn.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print(rows)
# print(type(rows))
for row in rows:
    print(row)
conn.close()
    
    
# connect > connection
# cursor > access 
# execute > SQL 
#     if write Commit 
    
# close        

# def connction: # db connection
    
    
# Def create db and table:
    
# def get_data(id,name,email):
#     id = input("enter Id")
#     name = input("enter Id")
#     email = input("enter Id")
# def add_data(id, email,name) :
#     get_data(id, email,name)
#     cursor.execute("INSERT INTO users (id , name, email) VALUES (%s,%s,%s)",(id,name,email))
#     print("Data added")
    
# def read