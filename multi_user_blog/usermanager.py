import json

class UserManager():
    """functions to add, amend and remove users"""

    def create_user(self, user):
        """takes in class instance  User(data), makes json, assigns ID#, 
        adds new user to file"""
        
        with open('user_data.txt', 'r') as f:
            all_lines = f.readlines()
            print (all_lines)
            last_line = all_lines[-1]
	    print(last_line)	
            last_user = json.loads(last_line)
            highest_id = last_user['id']
            new_id = int(highest_id) + 1
            new_user_dict = user.__dict__
            new_user_dict['id'] = new_id
        with open('user_data.txt', 'a') as outfile:
            outfile.write(json.dumps(new_user_dict) + '\n')
    
    def remove_user(self, user):
        """take in username, reads file, finds line with value matching
	argument, all non matching is added to array and then overwrite 
	to file """
        
	with open('user_data.txt', 'r') as f:
	    newlist = []
	    all_lines = f.readlines()
	    for line in all_lines:
		line_dict = json.loads(line)
		print (line_dict)
		username = line_dict['username']
		if username != user:
		    newlist.append(line_dict)
		    print(newlist)
	    f.close()
	with open('user_data.txt', 'w') as f:
	    f.seek(0)
	    print (newlist)	
	    for i in newlist:
		print(i)
                f.write(json.dumps(i) + "\n")
	    f.close()
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
