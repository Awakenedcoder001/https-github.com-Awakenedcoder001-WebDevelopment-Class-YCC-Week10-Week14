import abc
class Earth(abc.ABC):
    @abc.abstractmethod
    def Humain(self):
        pass

    def Culture(self):
        pass


class food(Earth):
    def chillicheese(self):
        self.vegetablename=input("Enter the vegetables to be chosen to eat tonight")
        print(f"The vegetable selected is : {self.vegetablename}")

obj=food()
obj.Humain()
obj.culture()
obj.chillicheese()