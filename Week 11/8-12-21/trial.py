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


n=int(input("Enter the number of employees : "))        
for i in range(n):
    age=int(input("Enter the Hero's age : " ))
    name=input("Enter the name of the Hero : " )
    role=input("Enter the heros roll in game : " )
    skill=input("Enter the heroes skill : " )


    hero1=Dota_Heroes(age=age,name=name,role=role,skill=skill)

    with open(file="Dota2heroes.txt", mode='wb')as file_write:
        pickle.dump(hero1,file_write)

print("Everything is stored inside object called Dota2heroes.txt")

file_read=open(file="Dota2heroes.txt", mode ='rb')
while True:
    try:
        hero_details=pickle.load(file_read)
        hero_details.display()
    
    except EOFError as msg:
        break;