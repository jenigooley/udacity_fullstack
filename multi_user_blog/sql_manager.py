import json
import sqlite3
import bcrypt

class UserManager():
    """functions to add, amend and remove users"""
    def __init__(self):
	self.conn = sqlite3.connect('./users.db')
	self.c = self.conn.cursor()

    def create_user(self, username, password, email):
        """takes user strings, inserts row in profiles db"""
	try:
	    self.c.execute("INSERT INTO profiles VALUES (?,?,?)", (username,
	    password, email))
	except sqlite3.IntegrityError: 
	    print("Somebody already has that name, try again.")
	self.conn.commit()	    
    
    def remove_user(self, username):
        """take  username string, querys db for username then deletes row from
	table """
	
	row = self.c.execute("SELECT * FROM profiles WHERE name =?",
	(username,))
	for i in row:
	    user = i[1]
	    print(user)
	    if user  == username:     
		self.c.execute("DELETE FROM profiles WHERE name=?", (username,))
		print("User was deleted")
		return True
	    
	    else:
		print ("Username not found, check your spelling homegirl.")
		return False
	self.conn.commit()
    
    def read_user(self, username):
        """take username string and returns readable user data"""

	self.c.execute("SELECT * FROM profiles WHERE name=?", (username,))
	print(self.c.fetchone())
	
	self.conn.commit()
