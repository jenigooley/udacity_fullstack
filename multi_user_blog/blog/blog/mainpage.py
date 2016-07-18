#get unicode value of each character in form data
#if item uni value btw 1 and 26 return return item + 13
# if item > uni value(m) return item - 13
# append item to string
#the loop back over result and return the none uni item

import webapp2
import jinja2
import string
import os
import re 

template_dir = os.path.join(os.path.dirname(__file__),"templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), 
autoescape=True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *arg, **kw):
        self.response.out.write(*arg, **kw) 
    

class Rot13(BaseHandler):
    def get(self):
        self.render("rot13.html")
    
    def post(self):
        rot13 = ''
        text = self.request.get("text")
        if text:
            rot13 = text.encode('rot13')
            self.render("rot13.html", text = rot13)

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and User_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return email and EMAIL_RE.match(email)
class SignUp(BaseHandler):

    def get(self):
        self.render("signup.html")

    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        params = dict(username = username, password = passoword, 
                      verify = verify, email = email)
        if not valid_username(username):
            params['error_username'] = "Thats not a valid username."
            have_error = True

        if not  valid_password(password):
            params['error_password'] = "That was not a valid passowrd"
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
            self.redirect('/welcome?username=' + username)

class Welcome(BaseHandler):
    def get(self):
        username = self.request.get('username')
        if valid_username(username):
            self.render('welcome.html', username = username)

app = webapp2.WSGIApplication([("/", Rot13)],
                                debug=True)

