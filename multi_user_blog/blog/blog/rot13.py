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

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__),"templates")
jinja_env = jinja.Enviornment(loader = jinja2.FileSystemLoader(template_dir), 
autoescape=True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BaseHandler(webapp2, RequestHandler):
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
            rot = str.maketrans("abcdefghijklmnopqrstuvwxyz",
                           "nopqrstuvwxyzabcdefghijklm")
            rerot =  form.translate(rot)
        self.render("rot13.html", text = rerot)
        
app = webapp2.WSDIApplication([("/rot13", Rot13)],
                                debug=True)

