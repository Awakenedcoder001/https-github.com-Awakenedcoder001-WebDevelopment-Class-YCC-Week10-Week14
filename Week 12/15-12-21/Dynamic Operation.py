#Steps to store data into the database
#connect()
#cursor()
#sql query --> Incomplete sql query
#execute(sqlquery, data)
#commit()

import mysql.connector

host = 'localhost'
port = 3306
user = 'root'
password = 'root'
database = 'Webdevelopment'

def disconnect(my_connection,my_cursor):
    if my_connection.is_connected():
        my_cursor.close()
        print('Cursor is connected')


def insert_operation():
    try:
        my_connection=mysql.connector.connect(host=host,port=port,user=user,password=password,database=database)
        print(f"Connection is established")

        my_cursor=my_connection.cursor()
        print(f"Cursor is created")

        sql_query = """Insert into webstudentdetails(ID,Name,Age,Gender,Emailid) Values(%s,%s,%s,%s,%s)"""
        print(f"Sql query is generated but incomplete")


        id = 1
        name = input("Enter the name : ")
        age = int(input("enter the age : "))
        gender = input("Enter the gender : ")
        email = input("enter the email : ")
        
        records=(id,name,age,gender,email)
        complete_query=(sql_query,records)
        my_cursor.execute(sql_query,records)
        print(f"Sql query is completed and executed")

        my_connection.commit()
        
    except mysql.connector.Error as msg:
        print(f"Casue of the exception is : {msg}")

    else :
        print("Data is saved sucessfully")

    finally :
        disconnect(my_connection,my_cursor)
        
if __name__ == "__main__":
    insert_operation()