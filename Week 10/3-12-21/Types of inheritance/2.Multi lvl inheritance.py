class WindowsXp: 
 def notepad(self): 
  print("Notepad is used to Write the important Information") 
 
 def wordpad(self): 
  print("wordpad is used to prepare documentation") 
 
class WindowVista(WindowsXp): 
 def performance(self): 
  print("Performane of Windows Vista is better then Windows XP") 
 
class Windows2003(WindowVista): 
 def games(self): 
  print("PUBG is a online game") 
 
w1=Windows2003() 
w1.notepad() 
w1.wordpad() 
w1.performance() 
w1.games()