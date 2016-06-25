import webapp2
import cgi


form="""
<form method="post">
    What is your birthday?
    <br>
    <label> Month <input type="text" name="month" value="%(month)s"></label>
    <label> Day <input type="text" name="day" value="%(day)s"></label>
    <label> Year <input type="text" name="year" value="%(year)s"></label>
    <div style="color: red">%(error)s</div>
    <br>
   <input type="submit">
</form>
"""

def escape_html(s):
    return cgi.escape(s, quote = True)

class MainPage(webapp2.RequestHandler):
    
    def valid_date(self, user_month, user_day, user_year):
               def valid_month(month):
                   months = ["January", "February", "March", "April", "May", 
                             "June", "July", "August", "September", "October", 
                             "November","December"]
                   abr_month = dict((m[:3].lower(),m)for m in months)
                   if month:
                       short_month = month[:3].lower()
                       return abr_month.get(short_month)

               def valid_day(day):
                    if day.isdigit() == True:
                        day = int(day)
                    if day in range(1,32):
                        return day

               def valid_year(year):
                   if year.isdigit() == True:
                       year = int(year)
                   if year in range(1900,2021):
                       return year
            
               month =valid_month(user_month)
               day = valid_day(user_day)
               year = valid_year(user_year)
                      
               if (month and day and year):
                   return True
                
    def write_form(self,error="", month="", day="", year=""):
        self.response.out.write(form % {"error": error, 
                                        "month":escape_html(month), 
                                        "day":escape_html(day), "year":(year)})

    def get(self):
        self.write_form()
    
    def post(self):
        user_month =self.request.get("month")
        user_day = self.request.get("day")
        user_year = self.request.get("year")
 
        if self.valid_date(user_month, user_day, user_year) == True:
            self.redirect("/thanks")            
        else:
            self.write_form("That doesn't look valid to me, buddy",
                            user_month, user_day, user_year )

class ThanksHandler(webapp2.RequestHandler):
        def get(self):
            self.response.write("Thanks, thats totally valid.")

app = webapp2.WSGIApplication([('/', MainPage), ('/thanks',ThanksHandler)],
                                 debug=True)

def main():
    app.run()

if __name__=='__main__':
    main()
