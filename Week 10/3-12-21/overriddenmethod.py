class WindowsXp(object): 
 """docstring for ClassName""" 
 def notepad(self): 
  print("NotePad is used to Write the important Info") 
 
 def wordpad(self): 
  print("WordPad is used to prepare documentation") 
 
 def performance(self): 
  print("Performane of Windows Xp is better then Windows 95") 
 
class WindowVista(WindowsXp): 
 def performance(self): 
  print("Performane of Windows Vista is better then Windows XP") 
  #Calling The Base Class(Parent Class) Method from Derived Class(Child Class) 
  WindowsXp().performance() 
 
w1=WindowVista() 
w1.notepad() 
w1.wordpad() 
w1.performance()