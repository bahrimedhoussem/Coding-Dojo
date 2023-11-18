class User :
    def __init__(self,first_name,last_name,email,age,points):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email 
        self.age = age
        self.enrolled_course = []
        self.points = points
    def display_info(self):
        print(f"first_name: {self.first_name} last_name: {self.last_name} , age: {self.age}")
    
    def spend_points(self, amount):
        if amount <= self.points:
            self.points -= amount
            print(f"first_name: {self.first_name} last_name: {self.last_name} spend {amount} points.")
        else:
            print(f"first_name: {self.first_name} last_name: {self.last_name} does not have enough points to spend.")
            print(f"Updated points: {updated_points}")
             
    def enroll (self):
        
        print(f"{self.first_name} {self.last_name} has enrolled in the course")

    

warrior= User("houssem","bahri","houssembahri011@gmail.com",27,5000)

user1=User("houssem","bahri","houssembahri011@gmail.com",27,5000)
user2=User("adrien","smith","adriensmith@gmail.com",31,4000) 
user3=User("bob","johnson","bobjohnson@gmail.com",32,4000)




user1.spend_points(50)  
user1.display_info()
warrior.spend_points(1000)
warrior.enroll()
user2.spend_points(80)
user2.display_info()
user3.display_info()
