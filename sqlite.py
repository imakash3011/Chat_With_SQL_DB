import sqlite3 #already come with python no need to install it

## To run this entire code use "python file_name" i.e. python sqlite.py
## connect to sqlite3
connection = sqlite3.connect("engg_student.db")

## create cursor object to insert record, create table
cursor = connection.cursor()

## create the table
table_info = """
create table Student (
Name Varchar(25), 
class varchar(25),
section varchar(25),
marks int 
)
"""

cursor.execute(table_info)

## Insert some records

cursor.execute(''' Insert into student values('Akash', 'Data Science', 'A', 100)''')
cursor.execute(''' Insert into student values('Saurabh', 'Data Analyst', 'B', 99)''')
cursor.execute(''' Insert into student values('Abhishek', 'Software Engineer', 'B', 96) ''')
cursor.execute(''' Insert into student values('Divanshu', 'Software Engineer', 'A', 91) ''')
cursor.execute(''' Insert into student values('Janak', 'DevOps', 'B', 94) ''')


## Display records
print("The inserted records are ")
data = cursor.execute( '''Select * from student ''' )

for row in data:
    print(row)


## Commit your changes in the database
connection.commit()
connection.close()