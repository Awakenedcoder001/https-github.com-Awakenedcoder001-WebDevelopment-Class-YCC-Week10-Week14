from abc import *
class Life:
    @abstractmethod
    def soul(self):
        pass
        print("Life has soul")

    @abstractmethod
    def thought(self):
        pass
        print("life has thoughts")

class Cat(Life):
    def trait(self):
        print("Dog walk")

    @abstractmethod
    def meow(self):
        print("cat meowss")

obj=Cat()
obj.trait()
obj.soul()
obj.thought()
