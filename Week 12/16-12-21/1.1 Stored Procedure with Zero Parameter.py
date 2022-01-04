# IN MY SQL 
# Creating the sql query inside stored Procedure :
# CREATE PROCEDURE noparameters()
# BEGIN
#  select * from cricketer;
# END

import mysql.connector

host='localhost'
port=3306
user='root'
password='root'
database='sport'

def stored_procedure():
 my_connection=mysql.connector.connect(host=host,port=port,user=user,password=password,database=database)

 my_cursor=my_connection.cursor()

 #procedurename
 procedurename='noparameters'

 #calling the procedure
 my_cursor.callproc(procedurename)

 #fetching the data :
 for records in my_cursor.stored_results():
  print(records)

  #data will be stored in the form of list of tuples
  result=records.fetchall()

 for i in result:
  print(i)

if __name__== '__main__':
 stored_procedure()