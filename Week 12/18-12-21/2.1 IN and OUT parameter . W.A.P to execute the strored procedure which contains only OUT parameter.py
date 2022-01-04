#W.A.P of stored procedure which accepts in and out parameter

import mysql.connector

host='localhost'
port=3306
user='root'
password='root'
database='sport'

def start_operation():
 try:
  my_connection=mysql.connector.connect(host=host,port=port,user=user,password=password,database=database)

  my_cursor=my_connection.cursor()

  procedurename='inoutparameter'

  #inputparameter
  the_department=input("ENTER THE TEAM NAME : ")

  #outputparameter
  the_count=0

  procdata=(the_department,the_count)

  results=my_cursor.callproc(procedurename,procdata)
  print(results)
 
 except mysql.connector.Error as msg:
  print(f"CAUSE OF THE EXECPTION IS : {msg}")

 else:
  # for i in range(len(results)):
  #  print(results[i])

  print(f"THE NAME OF THE TEAM IS : {the_department}")
  print(f"THE NO OF PLAYERS OF THE TEAM :{the_department} ARE : {results[1]}")
 finally:
  if my_connection.is_connected():
   my_cursor.close()

   my_connection.close()


if __name__== '__main__':
 start_operation()
 