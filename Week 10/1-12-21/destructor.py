import time 
class ClassName: 
 def __init__(self): 
  print("Inside The constructor") 
 
 def __del__(self): 
  print("Performing Clean Up activities") 
 
# t1=ClassName() 
# time.sleep(5) 
# t2=ClassName() 
# time.sleep(5) 
# t3=ClassName() 
# time.sleep(5) 
 
 
t1=ClassName() 
time.sleep(5) 
t2=t1 
time.sleep(5) 
t3=t2 
time.sleep(5)