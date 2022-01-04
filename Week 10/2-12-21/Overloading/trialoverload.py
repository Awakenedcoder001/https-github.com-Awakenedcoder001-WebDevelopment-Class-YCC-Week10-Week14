class Operation_Overloading:
    def __init__(self,name,number):
        self.name=name
        self.number=number
        
    def __add__(self,other):
        print(f"name is : {self.name +other.name}")
        print(f"Average is : {self.number+other.number/2}")

test1=Operation_Overloading(name="Tandin", number=31)
test2=Operation_Overloading(name="Tshewang", number=42)

test1+test2
         
