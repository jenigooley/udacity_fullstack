import json

class UserManager():
    def __init__(self):
        self.count = 0
    #create user id and add user data object to file
    def create_user(self, user):
        self.count += 1
        print (user)
        u_json = json.dumps(user.__dict__)
        print (u_json)
        with open('user_data.txt', 'w') as outfile:
            json.dump(u_json, outfile)
        return self.count 
    #remove user and user data from file
    def remove_user(self):
        user_database.remove(user)
    
    #display user data in browser with html
    def read_user(self):
        render(template)
        
