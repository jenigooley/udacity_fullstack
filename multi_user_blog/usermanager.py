import json

class UserManager():
    """functions to add, amend and remove users"""

    def create_user(self, user):
        """takes in class instance  User(data), makes json, assigns ID#, 
        adds new user to file"""
        
        with open('user_data.txt', 'r') as f:
            all_lines = list(f.readlines())
            last_line = all_lines[-1]
            last_user = json.loads(last_line)
            highest_id = last_user['id']
            new_id = int(highest_id) + 1
            new_user_dict = user.__dict__
            new_user_dict['id'] = new_id
        with open('user_data.txt', 'a') as outfile:
            outfile.write(json.dumps(new_user_dict) + '\n')
    
    def remove_user(self, user):
        """remove user and user data from file"""
        with open('user_data.txt', 'r+') as f:
            all_lines = list(f.readlines())
            for i in all_lines:
                line = json.loads(i)
                if user not in line:
                   f.write(line)
            return True

    def read_user(self, user):
        """display user data in browser with html"""
        try:
            f = open('user_data.txt', 'r')
            for i in f:
                d = json.loads(i)
            return d
        except:
            return False
