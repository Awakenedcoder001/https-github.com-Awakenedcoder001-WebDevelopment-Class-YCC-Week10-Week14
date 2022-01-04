class Human: 
 def talk(self): 
  print("Complex Langauge") 
 
class Dog: 
 """docstring for ClassName""" 
 def talk(self): 
  print("BOW BOW !!") 
 
class Cat: 
 def talk(self): 
  print("Meow Meow !!!") 
 
 
def speech(obj): 
 obj.talk() 
 #Human().talk() 
 #Dog().talk() 
 #Cat().talk() 
 
language=[Human(),Dog(),Cat()] 
 
 for obj in language: 
 speech(obj)