import webapp2
import datetime
from datetime import timedelta

# Time manipulation found in following source:
# http://stackoverflow.com/questions/18817750/python-datetime-add

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write("Welcome to Jeffrey Schachtsick's first Hello App")
        self.response.out.write('\n')
        time_diff = timedelta(hours=5)
        #the_time = datetime.datetime.now().strftime("%m-%d-%Y %H:%M")
        the_time = datetime.datetime.now()
        the_time -= timedelta(hours=7)
        the_time = the_time.strftime("%m-%d-%Y %H:%M")
        self.response.out.write('This is the current date and time in US-Pacific Time: ')
        self.response.out.write(the_time)

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

