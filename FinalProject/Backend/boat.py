#!/usr/bin/env python
# Author: Jeffrey Schachtsick
# CS 496 - Mobile/Cloud Development
# Final Project
# Subject: Fish Captian App
# File: boat.py
# Last Update: 11/16/2016
# source: Week 4 lecture 'API Demo'

# Imports
import webapp2
from google.appengine.ext import ndb
import db_models
import json

class Boat(webapp2.RequestHandler):
    def post(self):
        # Ensure we have application/json
        if 'application/json' not in self.request.accept:
            self.response.status = 406
            self.response.status_message = "Not Acceptable, Only supports JSON"
            self.response.write(self.response.status_message)
            return
        # Create a new boat and get the properties
        new_boat = db_models.Boat
        boat_name = self.request.get('boat_name', default_value=None)
        boat_type = self.request.get('boat_type', default_value=None)
        dock_city = self.request.get('dock_city', default_value=None)
        dock_state = self.request.get('dock_state', default_value=None)
        boat_fill = self.request.get('boat_fill', default_value=None)
        # Make sure we have a boat name, otherwise send an invalid message
        if boat_name:
            new_boat.boat_name = boat_name
        else:
            self.response.status = 400
            self.response.status_message = "Invalid request, Need a pet name"
            self.response.write(self.response.status_message)
        # Input values of boat type, dock city and state, and fish fill.  These are optional values
        if boat_type:
            new_boat.boat_type = boat_type
        if dock_city:
            new_boat.dock_city = dock_city
        if dock_state:
            new_boat.dock_state = dock_state
        if boat_fill:
            new_boat.boat_fill = boat_fill
        # Save all values into database
        key = new_boat.put()
        # Return the worker to write to display
        out = new_boat.to_dict()
        self.response.write(json.dumps(out))
        return

    def get(self, **kwargs):
        if 'application/json' not in self.request.accept:
            self.response.status = 406
            self.response.status_message = "Not Acceptable format, API must be JSON"
            self.response.write(self.response.status_message)
            return
        # if bid after /boat/.  See main
        if 'bid' in kwargs:
            try:
                out = ndb.Key(db_models.Boat, int(kwargs['bid'])).get().to_dict()
            except:
                self.response.write('Boat not found.')
                return
            self.response.write(json.dumps(out))
        else:
            q = db_models.Boat.query()
            keys = q.fetch(keys_only=True)
            results = { 'keys' : [x.id() for x in keys]}
            self.response.write(json.dumps(results))

class BoatSearch(webapp2.RequestHandler):
    def post(self):
        # Client must ask for an application/json representation in Accept header
        if 'application/json' not in self.request.accept:
            self.response.status = 406
            self.response.status_message = "Not Acceptable format, API must be JSON"
            return
        q = db_models.Boat.query()
        if self.request.get('boat_name', None):
            q = q.filter(db_models.Boat.boat_name == self.request.get('boat_name'))
        keys = q.fetch(keys_only=True)
        results = { 'keys' : [m.id() for m in keys]}
        self.response.write(json.dumps(results))