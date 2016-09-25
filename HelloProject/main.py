import webapp2
import datetime

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write("Welcome to Jeffrey Schachtsick's first Hello App")
        self.response.out.write('\n')
        the_time = datetime.datetime.now().strftime("%m-%d-%Y %H:%M")
        self.response.out.write('This is the current date and time: ')
        self.response.out.write(the_time)

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

