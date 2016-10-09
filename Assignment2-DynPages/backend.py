# Author: Jeffrey Schachtsick
# CS 496 - Mobile/Cloud Development
# Assignment 2: Dynamic Pages
# Subject: Car Inventory
# File: backend.py
# Last Update: 10/2/2016

import webapp2
import base_page
from google.appengine.ext import ndb
import db_defs

class Backend(base_page.CarInventory):
    # overriding the init function
    def __init__(self, request, response):
        self.initialize(request, response)
        self.template_values = {}


    def render(self, page):
        #self.template_values['features'] = [{'name':x.brand, 'key':x.key.urlsafe()} for x in db_defs.CarFeatures.query().fetch()]
        self.template_values['cars'] = [{'name':x.brand, 'key':x.key.urlsafe()} for x in db_defs.Car.query(ancestor=ndb.Key(db_defs.Car, self.app.config.get('default-group'))).fetch()]
        base_page.CarInventory.render(self, page, self.template_values)

    def get(self):
        self.render('carinventory.html')

    def post(self):
        # action is name of hidden field in backend.html
        action = self.request.get('action')
        # When adding car from backend.html, it will add car
        if action == 'add_car':
            # create a key with it's type and identifier(from car-data in main.py)
            key = ndb.Key(db_defs.Car, self.app.config.get('default-group'))
            #key2 = ndb.Key(db_defs.CarFeatures, self.app.config.get('default-group'))
            # call the constructor for car in db_defs
            car = db_defs.Car(parent=key)
            #feature = db_defs.CarFeatures(parent=key2)
            car.brand = self.request.get('car-brand')
            car.make = self.request.get('car-make')
            car.year = self.request.get('car-year')
            car.ctype = self.request.get('car-type')
            #car.special.append(str(self.request.get_all('car-special')))
            #car.special = self.request.get('car-special')
            for special in self.request.get_all('car-special'):
                car.special.append(special)
            car.condition = self.request.get('condition')

            #car.special = [ndb.Key(urlsafe=x) for x in self.request.get_all('car-special[]')]
            car.classes = [ndb.Key(urlsafe=x) for x in self.request.get_all('cars[]')]
            car.active = True
            car.put()
            #self.render('backend.html', {'message':'Added ' + car.name + ' to the database.'})
            self.template_values['message'] = 'Added car ' + car.brand + ' to the database.'
            #elif action == 'edit_car':
            #    key = ndb.Key(db_defs.Car, self.app.config.get('default-group'))
            #    car = db_defs.Car(parent=key)
            #    car.brand = self.request.get('class-name')
            #    cla.put()
            #    self.template_values['message'] = 'Added class ' + cla.name + ' to the database.'
        else:
            self.template_values['message'] = 'Action ' + action + ' is unknown.'
            #self.render('backend.html', {'message':'Action ' + action + ' is unknown.'})
        #self.template_values['classes'] = db_defs.CarClass.query(
        #   ancestor=ndb.Key(db_defs.CarClass, self.app.config.get('default-group'))).fetch()
        self.render('carinventory.html')