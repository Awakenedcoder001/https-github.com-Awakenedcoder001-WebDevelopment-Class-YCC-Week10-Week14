class Human: 
 def talk(self): 
  print("Complex Langauge") 
 
class Dog: 
 """docstring for ClassName""" 
 def bark(self): 
  print("BOW BOW !!") 
 
 
def speech(obj): 
 obj.talk() 
 #Human().talk() 
 #Dog().talk() 
 
language=[Human(),Dog()] 
 
for obj in language: 
 speech(obj)