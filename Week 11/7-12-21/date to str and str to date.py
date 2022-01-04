import datetime 
    
actual_date=datetime.datetime.now() 
print(actual_date) 
str_date=repr(actual_date) 
print(str_date) 
 
str_to_actual_date=eval(str_date) 
print(str_to_actual_date) 
 
 #2nd method

actual_date=datetime.datetime.now() 
print(actual_date) 
str_date=str(actual_date) 
print(str_date) 
 
str_to_actual_date=eval(str_date) 
print(str_to_actual_date)