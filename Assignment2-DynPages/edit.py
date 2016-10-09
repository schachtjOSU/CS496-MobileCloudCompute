# Author: Jeffrey Schachtsick
# CS 496 - Mobile/Cloud Development
# Assignment 2: Dynamic Pages
# Subject: Car Inventory
# File: edit.py
# Last Update: 10/2/2016

import webapp2
import base_page
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
import db_defs

class EditCar(base_page.CarInventory):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.template_values = {}
        #self.template_values['edit_url'] = blobstore.create_upload_url( '/edit/car' )

    #def render(self, page):
    #    #self.template_values['features'] = [{'name':x.brand, 'key':x.key.urlsafe()} for x in db_defs.CarFeatures.query().fetch()]
    #    self.template_values['cars'] = [{'name':x.brand, 'key':x.key.urlsafe()} for x in db_defs.Car.query(ancestor=ndb.Key(db_defs.Car, self.app.config.get('default-group'))).fetch()]
    #    base_page.CarInventory.render(self, page, self.template_values)

    def get(self):
        #if self.request.get('type') == 'car':
        car_key = ndb.Key(urlsafe=self.request.get('key'))
        car = car_key.get()
        self.template_values['car'] = car
        #features = db_defs.Car.special.query(ancestor=ndb.Key(db_defs.Car.special, self.app.config.get('default-group')))
        #feature_boxes = []
        #for f in features:
        #    if f in car.special:
        #       feature_boxes.append({'name':f.name, 'key':f.key.urlsafe(), 'checked':True})
        #    else:
        #        feature_boxes.append({'name':f.name, 'key':f.key.urlsafe(), 'checked':False})
        #self.template_values['classes'] = feature_boxes
        self.render('edit.html', self.template_values)

    def post(self):
        action = self.request.get('action')
        if action == 'edit_car':
            car_key = ndb.Key(urlsafe=self.request.get('key'))
            car = car_key.get()
            self.template_values['car'] = car
            #key = ndb.Key(db_defs.Car, self.app.config.get('default-group'))
            #car = db_defs.Car(parent=key)
            car.brand = self.request.get('car-brand')
            car.make = self.request.get('car-make')
            car.year = self.request.get('car-year')
            car.ctype = self.request.get('car-type')
            car.special = []
            for special in self.request.get_all('car-special'):
                car.special.append(special)
            car.condition = self.request.get('condition')
            car.classes = [ndb.Key(urlsafe=x) for x in self.request.get_all('cars[]')]
            car.active = True
            car.put()
            self.template_values['message'] = 'Edited a car of ' + car.brand + ' to the database.'
        else:
            self.template_values['message'] = 'Action ' + action + ' is unknown.'

        self.render('edit.html', self.template_values)