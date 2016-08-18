import json

class UserManager():
    
    def __init__(self):
        self.count = 0
    
    def create_user(self, user):
        """create user id and add user data object to file"""
        
        self.count += 1
        print (user)
        u_json = json.dumps(user.__dict__)
        print (u_json)
        with open('user_data.txt', 'w') as outfile:
            json.dump(u_json, outfile, '\n')
        return self.count 
    
    def remove_user(self, username):
        """remove user and user data from file"""
        
        f = open('user_data.txt', 'r')
        g = open ('data_user.txt', 'w')
           # d = r.readlines()
        #try:
        for i in f:
            d = json.loads(i)
            if d[0] != username:
                g.write(i)
        f.close()
        g.close()
        #except:
        #return False
    
    def read_user(self, user):
        """display user data in browser with html"""
        try:
            f = open('user_data.txt', 'r')
            for i in f:
                d = json.loads(i)
            return d
        except:
            return False
