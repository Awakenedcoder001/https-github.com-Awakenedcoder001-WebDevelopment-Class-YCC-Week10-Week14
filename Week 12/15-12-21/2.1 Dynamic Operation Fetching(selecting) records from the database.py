#Steps for Selecting a particular records form the database
#connect() 
#cursor() 
#sql_query() --> Incomplete 
#execute()  
#fetchone()

import mysql.connector 
 
host='localhost' 
port=3306 
user='root' 
password='root' 
database='webdevelopment' 
 
def select_operation(): 
 try:  
  my_connection=mysql.connector.connect(host=host,port=port,user=user,password=password,database=database) 
  print("CONNECTED TO THE DATABASE") 
 
  my_cursor=my_connection.cursor() 
  print("CURSOR IS CREATED") 
 
  sql_query="""SELECT * FROM studentdetails WHERE `id`=%s""" 
  print("SQL QUERY IS GENERATED BUT INCOMPLETE") 
 
  id=int(input("ENTER YOUR ID : ")) 
  id_student=(id,) 
  my_cursor.execute(sql_query,id_student) 
  print("SQL QUERY IS COMPLTED AND EXECUTED") 
 
  records=my_cursor.fetchone() 
  print(records) 
 
 except mysql.connector.Error as msg: 
  print(f"CAUSE OF THE EXCEPTION IS : {msg}") 
 
 else: 
  print("EXECUTED SUCCESSFULLY") 
 
 finally: 
  if my_connection.is_connected(): 
   my_cursor.close() 
   print("CURSOR IS CLOSED") 
 
   my_connection.close() 
   print("DATABASE CONNECTION IS CLOSED") 
 
if __name__== '__main__': 
 select_operation()