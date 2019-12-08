# HDip Data Analytics - Data Representation project 2019 
# Author Nigel Slack

# Called by the REST server 'server' to perform 'MySQL' CRUD operations on the 'cds' and
# 'dvds' tables

# Note : 'pip install mysql-connector' may be required first in the python environment
import mysql.connector

# Get the params for connecting to the database from a config file
import dbconfig as cfg

# Define a class to contain each operation
class projectDAO:

# First connect to the database   
    db=""
    def __init__(self):
       self.db=mysql.connector.connect(
       host=cfg.mysql['host'],
       user=cfg.mysql['user'],
       password=cfg.mysql['password'],
       database=cfg.mysql['database']
       )

# Write a record to 'cds'. Get back the id of the newly inserted record
    def createCd(self,values):
       cursor=self.db.cursor()
       sql="insert into cds  (album, artist, price) values (%s,%s,%s)"
       cursor.execute(sql,values)
       self.db.commit()
       return cursor.lastrowid

# Write a record to dvds'. Get back the id of the newly inserted record
    def createDvd(self,values):
       cursor=self.db.cursor()
       sql="insert into dvds  (title, director, price) values (%s,%s,%s)"
       cursor.execute(sql,values)
       self.db.commit()
       return cursor.lastrowid

# Get all records from'cds'
    def getAllCd(self):
       cursor=self.db.cursor()
       sql="select * from cds"
       cursor.execute(sql)
       results=cursor.fetchall()
       returnArray=[]
       for result in results:
           returnArray.append(self.convertToDictCd(result))
       return returnArray  

# Get all records from 'dvds'
    def getAllDvd(self):
       cursor=self.db.cursor()
       sql="select * from dvds"
       cursor.execute(sql)
       results=cursor.fetchall()
       returnArray=[]
       for result in results:
           returnArray.append(self.convertToDictDvd(result))
       return returnArray  

# Get one record from 'cds', using an input id value
    def findByIDCd(self,id):
       cursor=self.db.cursor()
       sql="select * from cds where id = %s"
       values = (id,)
       cursor.execute(sql,values)
       result=cursor.fetchone()
       return self.convertToDictCd(result)   

# Get one record from 'dvds', using an input id value
    def findByIDDvd(self,id):
       cursor=self.db.cursor()
       sql="select * from dvds where id = %s"
       values = (id,)
       cursor.execute(sql,values)
       result=cursor.fetchone()
       return self.convertToDictDvd(result)   

# Update a record in 'cds' using input values    
    def updateCd(self,values):
       cursor=self.db.cursor()
       sql="update cds set album = %s, artist = %s, price = %s where id = %s"
       cursor.execute(sql,values)
       self.db.commit()

# Update a record in 'dvds' using input values    
    def updateDvd(self,values):
       cursor=self.db.cursor()
       sql="update dvds set title = %s, director = %s, price = %s where id = %s"
       cursor.execute(sql,values)
       self.db.commit()

# Delete record from 'cds' using input id
    def deleteCd(self,id):
       cursor=self.db.cursor()
       sql="delete from cds where id = %s"
       values = (id,)
       cursor.execute(sql,values)

# Delete record from 'dvds' using input id
    def deleteDvd(self,id):
       cursor=self.db.cursor()
       sql="delete from dvds where id = %s"
       values = (id,)
       cursor.execute(sql,values)

# Convert 'cds' result to user friendly dictionary form    
    def convertToDictCd(self,result):
       colnames=["id","album","artist","price"]
       item={}
       if result:
           for i, colName in enumerate(colnames):
              value=result[i]
              item[colName]=value
       return item

# Convert 'dvds' result to user friendly dictionary form    
    def convertToDictDvd(self,result):
       colnames=["id","title","director","price"]
       item={}
       if result:
           for i, colName in enumerate(colnames):
              value=result[i]
              item[colName]=value
       return item

# Create instance of class
projectDAO = projectDAO()