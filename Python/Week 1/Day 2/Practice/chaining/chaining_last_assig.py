class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email 
        self.age = age 
        self.is_rewards_member = False
        self.gold_card_points = 0 
    
    def display_info(self):
        print(f'first name : {self.first_name} , last_name : {self.last_name} , age : {self.age}' )
        return self

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self  
        
    def spend_points(self,amount):
        if amount <= self.gold_card_points:
            self.gold_card_points -= amount
            print(f"first_name: {self.first_name} last_name: {self.last_name} spend {amount} points.")
        else:
            print(f"first_name: {self.first_name} last_name: {self.last_name} does not have enough points to spend.")
        return self 





user1=User("houssem","bahri","houssembahri011@gmail.com",27)
user2=User("adrien","smith","adriensmith@gmail.com",31) 
user3=User("bob","johnson","bobjohnson@gmail.com",32)


user1.display_info().enroll().spend_points(500) 