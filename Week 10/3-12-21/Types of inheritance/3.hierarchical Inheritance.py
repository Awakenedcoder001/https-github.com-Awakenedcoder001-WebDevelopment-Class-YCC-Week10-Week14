class UnixOs: 
 def shutdown(self): 
  print("Performing shutdow operation") 
 
 def start(self): 
  print("Performing start operation") 
 
class LinuxOs(UnixOs): 
 pass 
 
class WindowsOs(UnixOs): 
 pass 
 
class MacOs(UnixOs): 
 pass 
 

w3=LinuxOs() 
w3.shutdown() 
w3.start()


w2=WindowsOs() 
w2.shutdown() 
w2.start() 

w1=MacOs() 
w1.shutdown() 
w1.start() 
 

 
