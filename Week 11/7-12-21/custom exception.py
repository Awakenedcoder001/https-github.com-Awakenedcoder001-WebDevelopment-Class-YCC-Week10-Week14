import logging 
logging.basicConfig(filename="thazaybankwithcustomexception.txt",level=logging.DEBUG,format='%(asctime)s:: %(levelname)s :: %(message)s',datefmt="%d-%m-%y %H:%M:%S") 
 
class InsufficientFunds(Exception): 
    def __init__(self,msg): 
        self.msg=msg 
 
class InvalidEmailOrPassword(Exception): 
    def __init__(self,msg): 
        self.msg=msg 
 
class ServerDownError(Exception): 
    def __init__(self,msg): 
        self.msg=msg
