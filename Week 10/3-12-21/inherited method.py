class WindowsXp(object): 
 """docstring for ClassName""" 
 def notepad(self): 
  print("NotePad is used to Write the important Info") 
 
 def wordpad(self): 
  print("WOrdPad is used to prepare documentation") 
 
class WindowVista(WindowsXp): 
 pass 
 
w1=WindowVista() 
w1.notepad() 
w1.wordpad()