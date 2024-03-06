from flask_app.config.mysqlconnection import connectToMySQL

class User:
    DB = "users_schema"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
    
    
    @classmethod
    def save(cls, data):
        query = """INSERT INTO users (first_name,last_name,email)
    		    VALUES (%(first_name)s,%(last_name)s,%(email)s);"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"

        # comes back as the new row id
        result = connectToMySQL('users_schema').query_db(query,data)
        return result
        
    

    @classmethod
    def get_one(cls, user_id):
        query  = "SELECT * FROM users WHERE id = %(id)s;"
        data = {'id':user_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)
    
    @classmethod
    def remove(cls,data):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)
    @classmethod
    def edit(cls,data):
        query = """UPDATE users 
        SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s  
        WHERE id = %(id)s;"""
        return connectToMySQL(cls.DB).query_db(query,data)