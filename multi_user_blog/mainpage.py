import string
import os
import re 
import tornado.ioloop
import tornado.web
import test_create
import user_class

#template_path = os.path.join(os.path.dirname(__file__),"templates")

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return email and EMAIL_RE.match(email)

class BaseHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("signup.html")

    def post(self):
        have_error = False
        username = self.get_argument('username')
        password = self.get_argument('password')
        verify = self.get_argument('verify')
        email = self.get_argument('email')
        data = user_class.User(username, email, password)
        print (data) 
        params = dict(username = username, password = password, 
                      verify = verify, email = email)
        if not valid_username(username):
            params['error_username'] = "Thats not a valid username."
            have_error = True

        if not  valid_password(password):
            params['error_password'] = "That was not a valid   passowrd"
            have_error = True
        elif password != verify:
            params['error_verify'] =  "Your passwords didn't match"
            have_error = True
        
        if not valid_email(email):
            params['error_email'] = "That is not a valid email"
            have_error = True

        if have_error:
            self.render('signup.html')
        else:
            user_db = test_create.UserManager()
            user_db.create_user(data)
            self.redirect('/welcome?username='+ username)
            return data 

class WelcomeHandler(BaseHandler):
    def get(self):
        username = self.get_argument('username')
        self.render('welcome.html', username = username)

application = tornado.web.Application([
    (r"/*", BaseHandler),
    (r"/welcome", WelcomeHandler)
    ])

if __name__=="__main__":
    try:
        print ("started serving")
        application.listen(8080, "0.0.0.0")
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print ("server interrupted")
        tornado.ioloop.IOLoop.current().stop()

