import pickle
from firstpart_Creating_an_Object import Employee_Details

file_read=open(file="thazay_2.txt",mode='rb')
while True:
 try:
  employee_details=pickle.load(file_read)
  employee_details.display()

 except EOFError as msg:
  break;

 except Exception as msg:
  break;