#CLASS of Ninja
class Ninja:
    def__init__(self,first_name,last_name,treats,pet_food,pet): 
        self.first_name=first_name
        self.last_name=last_name
        self.treats=treats
        self.pet_food=pet_food
        self.pet=pet 

    def walk(self): #walks-walks th ninja's pet invoking the pet play () method
        self.pet.play()
    def bathe(self): 
        self.pet.noise()
    def bathe(self):
        self.pet.noise() 
#class of pet
class pet:
    def__init__(self,name,type,ticks,health,energy):
        self.name=name
        self.type=type
        self.ticks=ticks
        self.health=health
        self.energy=energy
#implement the following methods of class pet
    def sleep(self):
        self.energy+=25
    def eat (self):
        self.energy+=5
        self.health+=10 #walks-walks th ninja's pet invoking the pet play () method
    def noise(self):
        print(f'the sound of {self.name}')
                


  
