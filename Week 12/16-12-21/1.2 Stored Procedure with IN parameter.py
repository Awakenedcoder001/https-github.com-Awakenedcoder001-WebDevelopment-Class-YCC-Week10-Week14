#  In mysql
# CREATE PROCEDURE inputparameters(IN the_department varchar(45))
# BEGIN
#  select * from cricketer where designation=the_department;
# END
# W.A.P to input parameter in the stored procedure and display the details

import mysql.connector

host='localhost'
port=3306
user='root'
password='root'
database='sport'

def stored_procedure():
 try:
  my_connection=mysql.connector.connect(host=host,port=port,user=user,password=password,database=database)

  my_cursor=my_connection.cursor()

  #Procedure name
  procedurename='inputparameter'

  #Input to be sent to the stored procedure
  the_department=input("ENTER THE ROLE OF THE CRICKETER").lower()
  procdata=(the_department,)

  my_cursor.callproc(procedurename,procdata)

  for records in my_cursor.stored_results():
   result=records.fetchall()


 except mysql.connector.Error as msg:
  print(f"CAUSE OF THE ERROR IS : {msg}")

 else:
  print(f"THE DETAILS OF THE {the_department.upper()} ARE :")
  for data in result:
   print(data)

 finally:
  if my_connection.is_connected():
   my_cursor.close()
   my_connection.close()

if __name__== '__main__':
 stored_procedure()