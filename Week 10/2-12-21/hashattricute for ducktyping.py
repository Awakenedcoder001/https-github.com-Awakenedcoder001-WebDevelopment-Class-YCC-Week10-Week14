class Human: 
 def talk(self): 
  print("Complex Langauge") 
 
class Dog: 
 """docstring for ClassName""" 
 def bark(self): 
  print("BOW BOW !!") 
 
 
def speech(obj): 
 if hasattr(obj,'talk'): 
  obj.talk() 
 elif hasattr(obj,'bark'): 
  obj.bark() 
 else: 
  print("The Object Doenot Consits The method Specified") 
  
 
language=[Human(),Dog()] 
 
for obj in language: 
 speech(obj)