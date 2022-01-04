import abc 
class DbInterface(abc.ABC): 
 @abc.abstractmethod 
 def connect(self): 
  pass 
 
 @abc.abstractmethod 
 def disconnect(self): 
  pass 
 
class MySQL(DbInterface): 
 def connect(self): 
  print("Connected To MySQL DataBase") 
 
 def disconnect(self): 
  print("Disconnecting MySQL DataBase") 
 
class MongodB(DbInterface): 
 def connect(self): 
  print("Connected To MongodB DataBase") 
 
 def disconnect(self): 
  print("Disconnecting MongodB DataBase")  
 
 
dbname=input("ENTER THE DATABASE NAME AS MySQL or MongoDB") 
#Error : TypeError: String Name can not be callable  
db=dbname() 
db.connect() 
db.disconnect()