import gc 
print(gc.isenabled()) 
 
gc.disable() 
print(f'THE GARGABE COLLECTOR IS  ENABLED : {gc.isenabled()}') 
 
gc.enable() 
print(f'THE GARGABE COLLECTOR IS  ENABLED : {gc.isenabled()}')