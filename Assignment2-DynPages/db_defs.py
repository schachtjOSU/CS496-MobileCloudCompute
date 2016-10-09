# Author: Jeffrey Schachtsick
# CS 496 - Mobile/Cloud Development
# Assignment 2: Dynamic Pages
# Subject: Car Inventory
# File: db_defs.py
# Last Update: 10/2/2016

from google.appengine.ext import ndb
#import ndb

class Message(ndb.Model):
    car = ndb.StringProperty(required=True)
    date_time = ndb.DateTimeProperty(required=True)
    count = ndb.IntegerProperty(required=True)

class Car(ndb.Model):
    brand = ndb.StringProperty(required=True)
    make = ndb.StringProperty(required=True)
    year = ndb.StringProperty(required=True)
    ctype = ndb.StringProperty(required=False)
    special = ndb.StringProperty(repeated=True)
    condition = ndb.StringProperty(required=False)
    classes = ndb.KeyProperty(repeated=True)
    active = ndb.BooleanProperty(required=True)

class CarFeatures(ndb.Model):
    name = ndb.StringProperty(required=True)