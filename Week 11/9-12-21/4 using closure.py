import datetime 
def retirement(yob): 
 data="Years Left for retirement" 
 
 def retirement_slot(retiremnet_slot): 
  current_year=datetime.datetime.now().year 
  print(current_year) 
 
  current_age=current_year-yob 
  print(f"Current Age : {current_age}") 
 
  retiremnet_years=retiremnet_slot-current_age 
  print(f"{retiremnet_years} {data}") 
 
 return retirement_slot 
 
func1=retirement(1980) #address of retirement_slot address 
func1(60)