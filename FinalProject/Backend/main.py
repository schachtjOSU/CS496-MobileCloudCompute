#!/usr/bin/env python
# Author: Jeffrey Schachtsick
# CS 496 - Mobile/Cloud Development
# Final Project
# Subject: Fish Captian App
# File: main.py
# Last Update: 11/14/2016
# source: Week 4 lecture 'API Demo'

#imports
import webapp2

application = webapp2.WSGIApplication([
    ('/captian', 'captian.Captian'),
    ('/worker', 'worker.Worker'),
    ('/boat', 'boat.Boat'),
], debug=True)
application.router.add(webapp2.Route(r'/captian', 'captian.Captian'))
application.router.add(webapp2.Route(r'/captian/<cid:[0-9]+>/worker/<wid:[0-9]+><:/?>', 'captian.CaptWorkers'))
application.router.add(webapp2.Route(r'/captian/<cid:[0-9]+>/boat/<bid:[0-9]+><:/?>', 'captian.CaptBoats'))
application.router.add(webapp2.Route(r'/worker/<wid:[0-9]+><:/?>', 'worker.Worker'))
application.router.add(webapp2.Route(r'/worker/search', 'worker.WorkerSearch'))
application.router.add(webapp2.Route(r'/boat/<bid:[0-9]+><:/?>', 'boat.Boat'))
application.router.add(webapp2.Route(r'/boat/search', 'boat.BoatSearch'))