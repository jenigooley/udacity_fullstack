mport webapp2-2.5.2
import BaseHTTPServer
import cgi
import cgitb


form="""
<form method="post" action="processname.cgi">
    "What is your birthday?"
    <br>
    <label> Month
        <input type="text" name="month">
    </label>
    <label> Day
        <input type="text" name="day">
    </label>
    <label> Year
        <input type="text" name="year">
    </label>
    <br>
    <br>
   <input type="submit">
</form>
"""


class MainPage(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        """responds to a get request"""
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        self.wfile.write(form)

    def valid_date(self):
        form_data = cgi.FieldStorage()
        month = form_data.getvalue("month")
        print (month)
        day = form_data.getvalue("day")
        print(day)
        year = form_data.getvalue("year")
        print(year)
        
        
months = ["January", "February", "March", "April", "May", "June", "July",
                  "August", "September", "October", "November", "December"]
        abr_month = dict((m[:3].lower(),m)for m in months)
        def valid_month(month):
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

        user_month = valid_month(month)
        user_day = valid_day(day)
        user_year = valid_year(year)
        if ( user_month and user_day and user_year):
            return True


    def do_POST(self):
        """Respond to a POST request."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.valid_date()
        if valid_date() == False:
            self.response.wfile.write(form)
        else:
            self.response.wfile.write("Thanks! Thats a totally valid day!")

def run_server(MainPage):
    server_address = ('', 8080)
    http_s =BaseHTTPServer.HTTPServer(server_address,MainPage)

    print("now serving")
    try:
         http_s.serve_forever()
    except KeyboardInterrupt:
        http_s.server_close()
        print ("connection closed")

#app = webapp2.WSGIApplication([('/', MainPage)],
#                                 debug=True)
app = run_server(MainPage)
