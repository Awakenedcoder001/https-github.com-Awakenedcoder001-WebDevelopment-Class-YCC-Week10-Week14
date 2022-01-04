class Operator_overloading:
    def __init__(self,name,num):
        self.num=num

    def __mul__(self,other):
        print(f"Name is : {(self.num}*{other.num})")

s1=Operator_overloading(69)
s2=Operator_overloading(98)
s1*s2


s1=Operator_overloading(**)
s2=Operator_overloading(2)
s1*s2