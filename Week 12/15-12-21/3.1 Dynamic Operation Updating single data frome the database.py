import mysql.connector 
 
host='localhost' 
port=3306 
user='root' 
password='root' 
database='webdevelopments' 
 
def update_operation(): 
 try: 
  my_connection=mysql.connector.connect(host=host,port=port,user=user,password=password,database=database) 
  print("CONNECTION ESTABLISHED") 
 
  my_cursor=my_connection.cursor() 
  print("CURSOR IS CREATED") 
 
  sql_query="""UPDATE thazay SET `name`=%s WHERE `id`=4""" 
  print("SQL QUERY IS GENERATED BUT INCOMPLETE") 
 
  name=input("ENTER THE NAME TO UPDATE :") 
  #contact=int(input("ENTER THE NUMBER TO UPDATE :")) 
  records=(name,) 
 
  my_cursor.execute(sql_query,records) 
  print("SQL QUERY IS COMPLTED AND EXEUTED ") 
 
  my_connection.commit() 
  print("DATA IS UPDATED SUCCESSFULLY") 
 
 except mysql.connector.Error as msg: 
  print(f"CAUSE OF THE EXCEPTION IS : {msg}") 
 
 else: 
  print("DATA IS UPDATED SUCCESSFULLY") 
 
 finally: 
  if my_connection.is_connected(): 
   my_cursor.close() 
   print("CURSOR IS CLOSED") 
 
   my_connection.close() 
   print("DATABASE CONNECTION IS CLOSED") 
 
if __name__== '__main__': 
 update_operation()