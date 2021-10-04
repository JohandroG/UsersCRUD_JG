from users_app.config.mysqlconnection import connectToMySQL
#===========================================================================================================

class User:
    def __init__(self, data):

        self.id = data['id']
        self.first_name =  data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.update_at = data['updated_at']
#===========================================================================================================

    @classmethod
    def get_users_info(cls):
        query = "SELECT * FROM users;"

        result = connectToMySQL("users_schema").query_db(query)
        users = []

        for user in result:
            users.append(cls(user))
        return users
#===========================================================================================================

    @classmethod
    def addUser(cls,newUser):
        query = "INSERT INTO users(first_name,last_name,email,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s, SYSDATE(),SYSDATE())"
        data = {
            "first_name" : newUser[0],
            "last_name" : newUser[1],
            "email" : newUser[2]
        }
        result = connectToMySQL("users_schema").query_db( query, data )
        
        return result
#=========================================================================================
    @classmethod
    def showUserInfo(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        user_id = {
            "id" : data
        }
        result = connectToMySQL("users_schema").query_db( query, user_id )
        return result

#=========================================================================================
    @classmethod
    def editUser(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s WHERE id=%(id)s"

        newinfo = {
        "id": data[0],
        "first_name" : data[1],
        "last_name" : data[2],
        "email": data[3],
        }

        result = connectToMySQL( "users_schema" ).query_db( query, newinfo )
        return result

#=========================================================================================
    @classmethod
    def deleteuser(cls,id):
        
        query = "DELETE FROM users WHERE id = %(id)s"
        result = connectToMySQL("users_schema").query_db( query, id )
        return result










