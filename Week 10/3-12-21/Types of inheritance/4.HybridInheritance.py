class WindowsXp: 
 def notepad(self): 
  print("Notepad is used to Write the important Information") 
 
 def wordpad(self): 
  print("wordpad is used to prepare documentation") 
 
class WindowVista(WindowsXp): 
 pass 
 
class Windows2003(WindowVista): 
 pass 
 
class Windows2007(WindowVista): 
 pass 
 
w1=Windows2007() 
w1.notepad() 
w1.wordpad() 
 
w2=Windows2003() 
w2.notepad() 
w2.wordpad()