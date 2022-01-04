from abc import * 
class Fruits(ABC): 
 def taste(self): 
  print("Most of the fruits are sweet") 
 
 def season(self): 
  pass 
 
obj=Fruits()