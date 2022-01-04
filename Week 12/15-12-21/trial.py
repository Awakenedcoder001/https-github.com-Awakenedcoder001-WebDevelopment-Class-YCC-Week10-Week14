import mysql.connector

host = 'localhost'
port = 3306
user = 'root'
password = 'root'
database = 'networking'

def update_operation():
    my_connection=myl_connector.connect(host=host,port=port,user=user,password=password,database=database)
    print("Connection established")

    my_cursor=my_connection.cursor()
    print("Cursor is created")

    sql_query="""UPDATE `Tandin` SET 'name'=%s and 'contact' =%s where `id`=4"""
    print("SQL query is generated but incomplete")

    name = input("Enter the name to update")
    contact = int(input("Enter the updated number"))
    records=(name,contact)

    my_cursor.execute(sql_query,records)
    print("sql query is completed and ")

    