class Method_Overloading:
    def __init__(self):
        print("This is a constructor method")
        

    def add(self,a,b):
        sum=a+b
        return sum

    def add(self,a,b,c,d):
        sum = a +b+c
        return sum

    def add(self,a,b,c):
        sum = a+ b + c + d
        return sum
    
s1=Method_Overloading
res=s1.add(a=10,b=20,c=30,d=40)
print(res)

s1=Method_Overloading
res=s1.add(10,20)
print(res)