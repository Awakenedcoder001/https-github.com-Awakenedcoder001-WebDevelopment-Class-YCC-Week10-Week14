# creating an custumerise exception 
import logging  
logging.basicConfig(filename="thazaybankupdated.txt",level=logging.DEBUG,format='%(asctime)s:: %(levelname)s :: %(message)s',datefmt="%d-%m-%y %H:%M:%S")  
  
class InsufficientFunds(Exception):  
    def __init__(self,msg):  
        self.msg=msg  
  
class InvalidEmailOrPassword(Exception):  
    def __init__(self,msg):  
        self.msg=msg  
  
class ServerDownError(Exception):  
    def __init__(self,msg):  
        self.msg=msg 
 
# 2 ->part tiggering the exception 
acc_no=int(input("ENTER THE ACCOUNT NUMBER"))   
password=int(input("ENTER THE Password"))   
  
totalbalace=10000   
if acc_no == 5100061010001 and password == 123456789:   
    amount=int(input("ENTER THE AMOUNT TO WITHDRAW :")) #20000   
    logging.info(f"AMOUNT ENTERED TO WITHDRAW : {amount}" )  
    logging.info(f"TOTAL AMOUNT IN THE ACCOUNT BEFORE WITHDRAWING: {totalbalace}" )  
      
    balance=totalbalace-amount  #10000 - 20000 = -10000   
    if balance<0:  #balance=10000   
        balance=totalbalace   
        totalbalace=balance   
        msg="Insufficient Amount"  
        logging.error(msg)  
        raise InsufficientFunds(msg)#ZeroDIvisionError   
        
    else:   
        totalbalace=balance   
  
else:   
    msg="Invalid Email Or Password"  
    logging.error(msg)
    raise InvalidEmailOrPassword(msg)
