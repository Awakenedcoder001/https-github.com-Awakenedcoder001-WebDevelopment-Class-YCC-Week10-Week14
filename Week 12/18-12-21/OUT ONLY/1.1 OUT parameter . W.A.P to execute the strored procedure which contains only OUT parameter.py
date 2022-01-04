#W.A.P to execute the strored procedure which contains only OUT parameter

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

  procedurename='outparameter'

  #output paramerter
  the_count=0

  procdata=(the_count,)

  results=my_cursor.callproc(procedurename,procdata)
  print(f"THE NO OF BOWLERS PRESENT IN THE TEAM IS : {results}")

 except mysql.connector.Error as msg:
  print(f"CAUSE OF THE EXCEPTION IS : {msg}")

 finally:
  if my_connection.is_connected():
   my_cursor.close()

   my_connection.close()

if __name__== '__main__':
 start_operation()