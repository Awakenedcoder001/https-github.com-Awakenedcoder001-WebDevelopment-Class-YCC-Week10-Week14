import mysql.connector
host='localhost'
port=3306
user='root'
password='root'
database='transaction'

def helper():
	data=input("ENTER OK TO PERFORM CHANGES :").lower()
	if data=='ok':
		return True
	else:
		return False

def select_operation(my_connection,my_cursor):
	try:
		sql_query="SELECT * FROM `transactions`"
		print("SELECTING THE ENTIRE TABLE")

		my_cursor.execute(sql_query)
		print("SQL CUROR IS EXECUTED SUCCESSFULLY")

		records=my_cursor.fetchall()
		print(len(records))
		print(records)

	except mysql.connector.Error as msg:
		print(f"CAUSE OF THE EXCEPTION IS : {msg}")

	else:
		print("DATA IS DISPALYED SUCCESSFULLY")


def delete_operation(my_connection,my_cursor):
	sql_query="""DELETE FROM `transactions` WHERE id=%s"""
	print("SQL QUERY IS INCOMPLETE")

	id_student=int(input("ENTER THE ID TO OBE DELETED : "))
	id=(id_student,)
	my_cursor.execute(sql_query,id)

	condition=helper()
	
	if condition==True:
		select_operation(my_connection,my_cursor)
		my_connection.commit()
		print("DATA DELETED SUCCESSFULLY")

	else:
		my_connection.rollback()
		print("NO CHANGES PERFORMED")

def close_operation(my_connection,my_cursor):
	if my_connection.is_connected():
		my_cursor.close()
		print("CURSOR CONNECTION IS CLOSED")

		my_connection.close()
		print("DATABASE CONNECTION IS CLOSED")


def insert(my_connection,my_cursor):
	try:
		sql_query="""INSERT INTO `transactions`(`id`,`name`,`gender`,`contactno`,`emailid`) VALUES(%s,%s,%s,%s,%s)"""
		print("SQL QUERY IS GENERATED BUT INCOMPLETE")

		records=[]
		idstudent=4
		n=int(input("ENTER THE NO OF RECORDS"))
		for i in range(n):
			idstudent+=1
			name=input("ENTER THE NAME :")
			gender=input("ENTER THE GENDER")
			contact=int(input("ENTER THE CONTACT NUMBER :"))
			email=input("ENTER THE EMAIL ID :")
			records.append((idstudent,name,gender,contact,email))
			
		my_cursor.executemany(sql_query,records)
		print("SQL QUERY IS COMPLTED AND EXECUTED")

		condition=helper() #True / False
		print(condition)

		if condition==True:
			select_operation(my_connection,my_cursor)
			my_connection.commit()
			print("DATA IS STORED SUCCESSFULLY ")
			select_operation(my_connection,my_cursor)
		else:
			my_connection.rollback()
			print("DATA IS NOT STORED")

	except mysql.connector.Error as msg:
		print(f"CAUSE OF THE EXCEPTION IS : {msg}")


def update():
	my_connection=mysql.connector.connect(host=host,port=port,user=user,password=password,database=database)
	print("CONNECTION IS CREATED")

	my_cursor=my_connection.cursor()
	print("CURSOR IS CREATED")

	insert(my_connection,my_cursor)
	print(f"INSERTING THE DATA IN THE DATABASE IS SUCCESSFULL")

	select_operation(my_connection,my_cursor)
	print(f"DATA IN THE DATABASE BEFORE PERFORMING THE CHANGES")

	sql_query="""UPDATE `transactions` SET `gender`=%s WHERE `id`=2"""
	print(f"SQL QUERY IS GENERATED BUT INCOMPLETE")

	gender=input("ENTER THE GENDER :")

	records=(gender,)
	my_cursor.execute(sql_query,records)
	print("SQL QUERY IS COMPLTED AND UPDATED")

	select_operation(my_connection,my_cursor)
	print("BEFORMING PERFOMING UPDATE OPERATION")

	condition=helper()

	if condition==True:
		my_connection.commit()
		print(f"DATA IS UPDATED")
		select_operation(my_connection,my_cursor)
		print("AFTER PERFOMING UPDATE OPERATION")		

	else:
		my_connection.rollback()
		print("DATA IS NOT UPDATED")

	delete_data=input("ENTER THE YES OR NO TO DELETED ").lower()
	if delete_data=='yes':
		delete_operation(my_connection,my_cursor)
if __name__ == '__main__':
	update()