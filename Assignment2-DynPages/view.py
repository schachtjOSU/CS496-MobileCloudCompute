# Author: Jeffrey Schachtsick
# CS 496 - Mobile/Cloud Development
# Assignment 2: Dynamic Pages
# Subject: Car Inventory
# File: view.py
# Last Update: 10/2/2016

from google.appengine.ext import ndb
import base_page
import db_defs


class ViewCar(base_page.CarInventory):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.template_values = {}

    def get(self):
        #if self.request.get('type') == 'car':
        car_key = ndb.Key(urlsafe=self.request.get('key'))
        car = car_key.get()
        self.template_values['car'] = car
        #cars = db_defs.CarClass.query(ancestor=ndb.Key(db_defs.CarClass, self.app.config.get('default-group')))
        self.render('view.html', self.template_values)
