def outer_function(name):#2
    print("Inside of  outer_function")#3
    print(f" Name of the person is : {name}")#4

    def inner_function():#9
        print("inside inner function") #10
        print(f"Name of the person is : {name}") #11

    return inner_function#5
func1=outer_function("Thazay") #1  #6--> Address of inner function
print(func1)#7

func1()#8  #12
del outer_function()#13  --> Deleted outer function

func() #14

outer_function() Error

