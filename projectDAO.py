import mysql.connector
import dbconfig as cfg
class projectDAO:
    db=""
    def __init__(self):
       self.db=mysql.connector.connect(
       host=cfg.mysql['host'],
       user=cfg.mysql['user'],
       password=cfg.mysql['password'],
       database=cfg.mysql['database']
       )

    def createCd(self,values):
       cursor=self.db.cursor()
       sql="insert into cds  (album, artist, price) values (%s,%s,%s)"
       cursor.execute(sql,values)
       self.db.commit()
       return cursor.lastrowid

    def createDvd(self,values):
       cursor=self.db.cursor()
       sql="insert into dvds  (title, director, price) values (%s,%s,%s)"
       cursor.execute(sql,values)
       self.db.commit()
       return cursor.lastrowid

    def getAllCd(self):
       cursor=self.db.cursor()
       sql="select * from cds"
       cursor.execute(sql)
       results=cursor.fetchall()
       returnArray=[]
       for result in results:
           returnArray.append(self.convertToDictCd(result))
       return returnArray  

    def getAllDvd(self):
       cursor=self.db.cursor()
       sql="select * from dvds"
       cursor.execute(sql)
       results=cursor.fetchall()
       returnArray=[]
       for result in results:
           returnArray.append(self.convertToDictDvd(result))
       return returnArray  

    def findByIDCd(self,id):
       cursor=self.db.cursor()
       sql="select * from cds where id = %s"
       values = (id,)
       cursor.execute(sql,values)
       result=cursor.fetchone()
       return self.convertToDictCd(result)   

    def findByIDDvd(self,id):
       cursor=self.db.cursor()
       sql="select * from dvds where id = %s"
       values = (id,)
       cursor.execute(sql,values)
       result=cursor.fetchone()
       return self.convertToDictDvd(result)   

    def updateCd(self,values):
       cursor=self.db.cursor()
       sql="update cds set album = %s, artist = %s, price = %s where id = %s"
       cursor.execute(sql,values)
       self.db.commit()

    def updateDvd(self,values):
       cursor=self.db.cursor()
       sql="update dvds set title = %s, director = %s, price = %s where id = %s"
       cursor.execute(sql,values)
       self.db.commit()

    def deleteCd(self,id):
       cursor=self.db.cursor()
       sql="delete from cds where id = %s"
       values = (id,)
       cursor.execute(sql,values)

    def deleteDvd(self,id):
       cursor=self.db.cursor()
       sql="delete from dvds where id = %s"
       values = (id,)
       cursor.execute(sql,values)

    def convertToDictCd(self,result):
       colnames=["id","album","artist","price"]
       item={}
       if result:
           for i, colName in enumerate(colnames):
              value=result[i]
              item[colName]=value
       return item

    def convertToDictDvd(self,result):
       colnames=["id","title","director","price"]
       item={}
       if result:
           for i, colName in enumerate(colnames):
              value=result[i]
              item[colName]=value
       return item

projectDAO = projectDAO()