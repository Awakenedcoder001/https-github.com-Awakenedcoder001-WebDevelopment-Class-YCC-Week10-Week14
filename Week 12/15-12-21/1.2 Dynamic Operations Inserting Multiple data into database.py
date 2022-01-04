#Steps to follow to store the data to the database using dynamic operations 
#connect() 
#cursor() 
#sql query --> Incomplete sql query 
#execute(sqlquery,data) 
#commit() 
 
host='localhost' 
port=3306 
user='root' 
password='root' 
database='webdevelopment' 
 
import mysql.connector 
def disconnect(my_connection,my_cursor): 
 if my_connection.is_connected(): 
  my_cursor.close() 
  print("CURSOR CONNECTION IS CLOSED") 
 
  my_connection.close() 
  print("DATABASE CONNECTION IS CLOSED") 
 
def insert_operation(): 
 try: 
  my_connection=mysql.connector.connect(host=host,port=port,user=user,password=password,database=database) 
  print(f"CONNECTION IS ESTABLISHED") 
 
  my_cursor=my_connection.cursor() 
  print("CURSOR IS CREATED") 
   
  sql_query="""INSERT INTO studentdetails(id,name,age,gender,email) VALUES(%s,%s,%s,%s,%s)""" 
  print("SQL QUERY IS GENERATED BUT INCOMPLETE") 
   
 
  records=[] 
  idstudent=3 
  for i in range(5): 
   idstudent+=1 
   name=input("ENTER THE NAME :") 
   age=int(input("ENTER THE AGE :"))  
   gender=input("ENTER THE GENDER :") 
   email=input("ENTER THE EMAID ID :") 
   records.append((idstudent,name,age,gender,email)) 
   
   
  my_cursor.executemany(sql_query,records) 
  print(f"SQL QUERY IS COMPLETED AND EXECUTED") 
 
  my_connection.commit() 
 
 except mysql.connector.Error as msg: 
  print(f"CAUSE OF THE EXCEPTION IS : {msg}") 
 
 else: 
  print("DATA IS SAVED SUCCESSFULLY") 
  
 finally: 
  disconnect(my_connection,my_cursor) 
    
 
if __name__== '__main__': 
 insert_operation()