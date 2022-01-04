import mysql.connector 
 
host='localhost' 
port=3306 
user='root' 
password='root' 
database='university' 
 
def disconnect(my_connection,my_cursor): 
 if my_connection.is_connected(): 
  my_cursor.close() 
  print(f"CURSOR IS CLOSED SUCCESSFULLY") 
  my_connection.close() 
  print(f"DATABSE CONNECTION IS CLOSED") 
 
def insert_operation(): 
 try: 
  #Established the connnection with the database 
  my_connection=mysql.connector.connect(host=host,port=port,user=user,password=password,database=database) 
  print(f"CONNECTED TO THE DATABASE SUCCESSFULLY WITH NAME : {database}") 
 
  #Creating the cursor for communicating with the tables in the database 
  my_cursor=my_connection.cursor() 
  print(f"CURSOR IS CREATED") 
 
  #Generating the sql query 
  #sql_query="""INSERT INTO student`(`id,name,gender,age,`course`) VALUES(1,"PEMBA","MALE",31,"WEB DEVELOPMENT")""" 
  sql_query="""INSERT INTO student VALUES(3,"CHANDRA","SHEMALE",69,"WEB DEVELOPMENT")""" 
  print(f"SQL QUERY IS CREATED") 
 
  #Executing the sql query 
  my_cursor.execute(sql_query) 
  print(f"SQL QUERY IS EXECUTED SUCCESSFULLY !!!") 
 
  #Stored the data into the database 
  my_connection.commit() 
  print("DATA IS STORED IN THE DATABASE SUCCESSFULLY!!") 
 
 except mysql.connector.Error as msg: 
  print(f"CAUSE OF THE EXCEPTION IS : {msg}") 
 
 else: 
  print("NO ERRORS OCCURRED DURING THE EXECUTION") 
 
 finally: 
  disconnect(my_connection,my_cursor) 
 
if __name__== '__main__': 
 insert_operation()