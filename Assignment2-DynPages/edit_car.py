# Author: Jeffrey Schachtsick
# CS 496 - Mobile/Cloud Development
# Assignment 2: Dynamic Pages
# Subject: Car Inventory
# File: edit_car.py
# Last Update: 10/2/2016

import webapp2
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import db_defs
import base_page


class EditCar():
    def post(self):
        car_key = ndb.Key(urlsafe=self.request.get('key'))
        car = car_key.get()
        car.classes = [ndb.Key(urlsafe=x) for x in self.request.get_all('classes[]')]
        car.put()
        self.redirect('/edit?key=' + car_key.urlsafe() + '&type=car')