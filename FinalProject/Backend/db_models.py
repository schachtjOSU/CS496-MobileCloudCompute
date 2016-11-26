#!/usr/bin/env python
# Author: Jeffrey Schachtsick
# CS 496 - Mobile/Cloud Development
# Final Project
# Subject: Fish Captian App
# File: db_models.py
# Last Update: 11/14/2016
# source: Week 4 lecture 'API Demo'

#import ndb
from google.appengine.ext import ndb

class Model(ndb.Model):
    def to_dict(self):
        # Call the super to pull the key id
        d = super(Model, self).to_dict()
        d['key'] = self.key.id()
        return d

# Class for Captian
class Captian(Model):
    capt_name = ndb.StringProperty(required=True)
    capt_city = ndb.StringProperty()
    capt_state = ndb.StringProperty()
    total_take = ndb.IntegerProperty()
    worker_list = ndb.KeyProperty(repeated=True)
    boat_list = ndb.KeyProperty(repeated=True)

    # Return list of workers the captian has.
    def to_dict(self):
        d = super(Captian, self).to_dict()
        d['worker_list'] = [w.id() for w in d['worker_list']]
        return d

    # Return list of boats the captian has.
    def to_dict(self):
        t = super(Captian, self).to_dict()
        t['boat_list'] = [b.id() for b in t['boat_list']]
        return t

# Class for workers
class Worker(Model):
    worker_name = ndb.StringProperty(required=True)
    worker_city = ndb.StringProperty()
    worker_state = ndb.StringProperty()
    worker_take = ndb.IntegerProperty()

# Class for Boats
class Boat(Model):
    boat_name = ndb.StringProperty(required=True)
    boat_type = ndb.StringProperty()
    dock_city = ndb.StringProperty()
    dock_state = ndb.StringProperty()
    boat_fill = ndb.IntegerProperty()