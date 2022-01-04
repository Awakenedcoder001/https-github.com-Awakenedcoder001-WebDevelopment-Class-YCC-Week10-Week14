import mysql.connector
if __name__=='__main__':
    try:
        host = 'localhost'
        port = 3306
        user = 'root'
        password = 'root'
        database = 'student'
        my_connect = mysql.connector.connect(host=host,port=port,user=user,password=password,database=database)

        print(f"Database connected with : {database}")
        print(f"pawword is stored in : {password}")    
    
    except mysql.error as msg:
        print(f"cause of exception is  : {msg}")

    except Exception as msg:
        print(f"Cause of the exceptio nis : {msg}")
    
    else:
        print("Excequted sucessfully")

    finally:
        my_connect.close()
        print("execution finished")