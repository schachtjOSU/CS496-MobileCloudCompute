import webapp2
import datetime         # for getting the current time

class MainHandler(webapp2.RedirectHandler):
    def getTime(self):
        """Return the current date and time"""
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.response.write('This is the current time: ', current_time)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

#@app.errorhandler(404)
#def page_not_found(e):
#    """Return a custom 404 error."""
#    return 'Sorry, nothing at this URL.', 404
