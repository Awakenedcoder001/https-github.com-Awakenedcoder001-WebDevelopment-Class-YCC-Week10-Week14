class Humain:
    def talk(self):
        print("Complex Language")


class Dog:
    """docstring for ClassName"""
    def talk(self):
        print("Woof Woof!!")

class Cat:
    def talk(self):
        print("Meow Meow!!")
    
def speech(obj):
    obj.talk()
    #Humain.talk()
    #Dog.talk()
    #Cat.talk()

    
language=[Humain(),Dog(),Cat()]
for obj in language:
    speech(obj)



