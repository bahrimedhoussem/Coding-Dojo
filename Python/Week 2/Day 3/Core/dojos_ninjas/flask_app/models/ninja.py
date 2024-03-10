from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Ninja:
    def __init__ (self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.dojos_id=data["dojos_id"]

    @classmethod
    def save(cls, data):
        query = """INSERT INTO ninjas (first_name,last_name,age,dojos_id) VALUES  VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"""

        # comes back as the new row id
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result
    
    @classmethod
    def get_one(cls, data):
        query  = "SELECT * FROM ninjas WHERE ninja.id = %(id)s;"
        
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
