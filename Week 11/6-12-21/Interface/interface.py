from abc import * 
class Plane(ABC): 
 @abstractmethod 
 def fly(self): 
  pass 
 
 @abstractmethod 
 def carry(self): 
  pass 
 
 @abstractmethod 
 def takeoff(self): 
  pass 
 
class Cargo(Plane): 
 def fly(self): 
  print("Cargo plane is flying") 
 
 def carry(self): 
  print("Cargo Plane is carrying cargo") 
 
 def takeoff(self): 
  print("Cargo Plane is takeingoff from cargo port") 
 
class Fighter(Plane): 
 def fly(self): 
  print("Fighter plane is flying") 
 
 def carry(self): 
  print("Fighter Plane is carrying Military troops") 
 
 def takeoff(self): 
  print("Fighter Plane takes off from Military port") 
 
class Passenger(Plane): 
 def fly(self): 
  print("Passenger plane is flying") 
 
 def carry(self): 
  print("Passenger Plane is carrying passenger") 
 
 def takeoff(self): 
  print("Passenger Plane takes off from airport") 
 
obj=Passenger() 
obj.fly() 
obj.carry() 
obj.takeoff() 
 
obj1=Fighter() 
obj1.fly() 
obj1.carry() 
obj1.takeoff() 
 
obj2=Cargo() 
obj2.fly() 
obj2.carry() 
obj2.takeoff()