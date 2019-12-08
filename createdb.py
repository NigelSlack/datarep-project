# HDip Data Analytics - Data Representation project 2019 
# Author Nigel Slack

# Create a 'mysql' database called 'datarepresentation', if it does not exist
# Create 2 tables 'cds' and 'dvds' in the database, if they do not exist
# Write 3 sample records into each table

# 'cds' format :
#   id       int               key created by sql
#   album    varchar(255)      album name
#   artist   varchar(255)      artist/band name
#   price    int               price as simple integer, eg 800 for €8.00

# 'dvds' format :
#   id       int               key created by sql
#   title    varchar(255)      film title
#   director varchar(255)      director name
#   price    int               price as simple integer, eg 800 for €8.00

# Note : 'pip install mysql-connector' may be required first in the python environment
import mysql.connector

# Get the params for connecting to the database from a config file
import dbconfig as cfg

# Connect to mysql, without specifying a database
db=mysql.connector.connect(
    host=cfg.mysql['host'],
    user=cfg.mysql['user'],
    password=cfg.mysql['password']
)

# Check if the database already exists
# (ref https://stackoverflow.com/questions/44893565/get-list-of-mysql-databases-with-python)
cursor=db.cursor()
cursor.execute("SHOW DATABASES")
dbexists=False
for x in cursor:
  if 'datarepresentation' in x:
      dbexists=True

# If the database doesn't yet exist, create it
if not dbexists:
   cursor.execute("CREATE DATABASE datarepresentation") 
   print('\n Database "datarepresentation" created')

# Close the cursor, then re-open it, this time specifying the database
cursor.close()
db=mysql.connector.connect(
    host=cfg.mysql['host'],
    user=cfg.mysql['user'],
    password=cfg.mysql['password'],
    database=cfg.mysql['database']
)

cursor=db.cursor()

# Check to see if the 'cds' table already exists
cursor.execute("SELECT * FROM information_schema.tables WHERE table_name = 'cds'")
result = cursor.fetchall()

# If the table doesn't exist, create it
if not result:
    sql="CREATE TABLE cds (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,album VARCHAR(255),artist VARCHAR(255),price INT)"
    cursor.execute(sql)
    print('\nCreated table "cds" in database "datarepresentation"')

# Check to see if the 'dvds' table already exists
cursor.execute("SELECT * FROM information_schema.tables WHERE table_name = 'dvds'")
result = cursor.fetchall()

# If the table doesn't exist, create it
if not result:
    sql="CREATE TABLE dvds (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,title VARCHAR(255),director VARCHAR(255),price INT)"
    cursor.execute(sql)
    print('\nCreated table "dvds" in database "datarepresentation"')    

# Insert then delete a temporary record for each table. This gets round a problem
# where the web page displays data incorrectly if a record with id = 1 is updated
# in the 'dvds' table.
sql="insert into cds (album, artist, price) values (%s,%s,%s)"
values = ("temp","temp",10)
cursor.execute(sql,values)
sql="insert into dvds (title, director, price) values (%s,%s,%s)"
values = ("temp","temp",10)
cursor.execute(sql,values)
db.commit()
sql="delete from cds"
cursor.execute(sql)
sql="delete from dvds"
cursor.execute(sql)
db.commit()

# Insert 3 sample records into 'cds'
print('\nInserting records into table "cds"')
sql="insert into cds (album, artist, price) values (%s,%s,%s)"
values = ("Searchlight","Runrig",1000)
cursor.execute(sql,values)
sql="insert into cds (album, artist, price) values (%s,%s,%s)"
values = ("Delerium","Capercaillie",1200)
cursor.execute(sql,values)
sql="insert into cds (album, artist, price) values (%s,%s,%s)"
values = ("Live in Spain","Skyedance",700)
cursor.execute(sql,values)
db.commit()

# Display what's in the table
print('\nEntries in table "cds" -\n')
sql="select * from cds"
cursor.execute(sql)
result = cursor.fetchall()
for x in result:
    print(x)

# Insert 3 sample records into 'dvds'
print('\nInserting records into table "dvds"')
sql="insert into dvds (title, director, price) values (%s,%s,%s)"
values = ("Brooklyn","John Crowley",650)
cursor.execute(sql,values)
sql="insert into dvds (title, director, price) values (%s,%s,%s)"
values = ("Lost in Translation","Sofia Coppola",1200)
cursor.execute(sql,values)
sql="insert into dvds (title, director, price) values (%s,%s,%s)"
values = ("Atonement","Joe Wright",900)
cursor.execute(sql,values)
db.commit()

# Display what's in the table
print('\nEntries in table "dvds" -\n')
sql="select * from dvds"
cursor.execute(sql)
result = cursor.fetchall()
for x in result:
    print(x)

# Some other potential useful commands
#sql="select * from student where id = %s"
# values = (1,)

#sql=("update book set price = %s where id = %s")
#values = (2200,1)

#sql="delete from student where id = %s"
#values = (1,)


