from abc import *
class Life:
    @abstractmethod
    def soul(self):
        pass

    @abstractmethod
    def thought(self):
        pass

class Cat(life):
    def trait(self):
        print("Dog walk")

    @abstractmethod
    def meow(self):
        print("cat meowss")

obj=Cat()
obj.trait()
obj.meow()
obj.thought()
