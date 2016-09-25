import webapp2
#import datetime         # for getting the current time

class MainHandler(webapp2.RedirectHandler):
    def getTime(self):
        """Return the current date and time"""
        #current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        #self.response.write('This is the current time: ', current_time)
        self.response.write('This is the current time: ')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)

