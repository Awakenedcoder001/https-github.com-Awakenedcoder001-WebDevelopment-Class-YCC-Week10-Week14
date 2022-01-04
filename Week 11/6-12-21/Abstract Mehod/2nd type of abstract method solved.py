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
 
 
dbname=input("ENTER THE DATABASE NAME AS MySQL or MongoDB :") 
 
#Converting the string name into the class name 
db=globals()[dbname] 
print(db) 
 
#Creating an object of the class: 
classname=db() 
 
#Calling the instance methods using obj reference 
classname.connect() 
classname.disconnect()