class WindowsXp: 
 def notepad(self): 
  print("Notepad is used to Write the important Information") 
 
 def wordpad(self): 
  print("wordpad is used to prepare documentation") 
 
class WindowVista(WindowsXp): 
 pass 
 
w1=WindowVista() 
w1.notepad() 
w1.wordpad()