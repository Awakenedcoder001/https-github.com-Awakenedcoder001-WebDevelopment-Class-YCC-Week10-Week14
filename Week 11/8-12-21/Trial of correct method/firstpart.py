import pickle
class Dota_Heroes:
    def __init__(self,name,age,role,skill):
        self.age = age
        self.name= name
        self.role = role
        self.skill = skill

    def display(self):
        print(f"Name of the hero is : {self.name}")
        print(f"Age of the hero is : {self.age}")
        print(f"The Heroes role in the game is that of a : {self.role}")
        print(f"The skill the Hero holds is {self.skill}")
