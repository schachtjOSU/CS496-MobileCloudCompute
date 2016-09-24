from flask import Flask
import datetime         # for getting the current time
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def getTime():
    """Return the current date and time"""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    return 'The current date and time is: ', current_time


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
