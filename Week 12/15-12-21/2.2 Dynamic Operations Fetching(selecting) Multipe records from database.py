#steps to select  Multiple operation:
#connect(5 parameters) 
#cursor() 
#sql_query 
#execute(sql_query) 
#executeall()

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
 
  #Selecting the sql query 
  sql_query="""SELECT * FROM `student`""" 
  print(f"SQL QUERY IS CREATED") 
 
  #Executing the sql query 
  my_cursor.execute(sql_query) 
  print(f"SQL QUERY IS EXECUTED SUCCESSFULLY !!!") 
 
  records=my_cursor.fetchall() 
  print(records) 
 
  for i in records: 
   print(i) 
 
 except mysql.connector.Error as msg: 
  print(f"CAUSE OF THE EXCEPTION IS : {msg}") 
 
 else: 
  print("NO ERRORS OCCURRED DURING THE EXECUTION") 
 
 finally: 
  disconnect(my_connection,my_cursor) 
 
if __name__== '__main__': 
 insert_operation()


#output
# CONNECTED TO THE DATABASE SUCCESSFULLY WITH NAME : university 
# CURSOR IS CREATED 
# SQL QUERY IS CREATED 
# SQL QUERY IS EXECUTED SUCCESSFULLY !!! 
# [(1, 'PEMBA', 'MALE', 31, 'WEB DEVELOPMENT'), (3, 'CHANDRA', 'SHEMALE', 69, 'WEB DEVELOPMENT')] 
# (1, 'PEMBA', 'MALE', 31, 'WEB DEVELOPMENT') 
# (3, 'CHANDRA', 'SHEMALE', 69, 'WEB DEVELOPMENT') 
# NO ERRORS OCCURRED DURING THE EXECUTION 
# CURSOR IS CLOSED SUCCESSFULLY 
# DATABSE CONNECTION IS CLOSED