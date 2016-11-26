#!/usr/bin/env python
# Author: Jeffrey Schachtsick
# CS 496 - Mobile/Cloud Development
# Final Project
# Subject: Fish Captian App
# File: captian.py
# Last Update: 11/16/2016
# source: Week 4 lecture 'API Demo'

# imports
import webapp2
from google.appengine.ext import ndb
import db_models
import json

class Captian(webapp2.RequestHandler):
    def post(self):
        if 'application/json' not in self.request.accept:
            self.response.status = 406
            self.response.status_message = "Not Acceptable, Only supports JSON"
            self.response.write(self.response.status_message)
            return
        # Create new structure
        new_captian = db_models.Captian()
        capt_name = self.request.get('capt_name', default_value=None)
        capt_city = self.request.get('capt_city', default_value=None)
        capt_state = self.request.get('capt_state', default_value=None)
        total_take = self.request.get('total_take', default_value=None)
        worker_list = self.request.get_all('worker_list[]', default_value=None)
        boat_list = self.request.get_all('boat_list[]', default_value=None)
        # Does the captian name exist, then add the struct.  Otherwise display error
        if capt_name:
            new_captian.capt_name = capt_name
        else:
            self.response.status = 400
            self.response.status_message = "Invalid request"
            self.response.write(self.response.status_message)
        # See if the other optional elements exist
        if capt_city:
            new_captian.capt_city = capt_city
        if capt_state:
            new_captian.capt_state = capt_state
        if total_take:
            new_captian.total_take = total_take
        if worker_list:
            for worker in worker_list:
                new_captian.worker_list.append(ndb.Key(db_models.Worker, int(worker)))
        else:
            self.response.status = 400
            self.response.status_message = "Invalid request"
            self.response.write(self.response.status_message)
        if boat_list:
            for boat in boat_list:
                new_captian.boat_list.append(ndb.Key(db_models.Boat, int(boat)))
        else:
            self.response.status = 400
            self.response.status_message = "Invalid request"
            self.response.write(self.response.status_message)
        key = new_captian.put()
        out = new_captian.to_dict()
        self.response.write(json.dumps(out))
        return

class CaptWorkers(webapp2.RequestHandler):
    def put(self, **kwargs):
        if 'application/json' not in self.request.accept:
            self.response.status = 406
            self.response.status_message = "Not Acceptable, Only supports JSON"
            self.response.write(self.response.status_message)
            return
        if 'cid' in kwargs:
            captian = ndb.Key(db_models.Captian, int(kwargs['cid'])).get()
            if not captian:
                self.response.status = 404
                self.response.status_message = "Captian Not Found."
                self.response.write(self.response.status_message)
                return
            if 'wid' in kwargs:
                worker = ndb.Key(db_models.Worker, int(kwargs['wid']))
                if not worker:
                    self.response.status = 404
                    self.response.status_message = "Worker Not Found"
                    self.response.write(self.response.status_message)
                    return
            if worker not in captian.worker_list:
                captian.worker_list.append(worker)
                captian.put()
            else:
                self.response.status = 404
                self.response.status_message = "No Worker Duplicates"
                self.response.write(self.response.status_message)
                return
            self.response.write(json.dumps(captian.to_dict()))
            return

    # Remove a worker from the captian
    def delete(self, **kwargs):
        if 'application/json' not in self.request.accept:
            self.response.status = 406
            self.response.status_message = "Not Acceptable, Only supports JSON"
            self.response.write(self.response.status_message)
            return
        if 'cid' in kwargs:
            captian = ndb.Key(db_models.Captian, int(kwargs['cid'])).get()
            if not captian:
                self.response.status = 404
                self.response.status_message = "Captian Not Found."
                self.response.write(self.response.status_message)
                return
            if 'wid' in kwargs:
                worker = ndb.Key(db_models.Worker, int(kwargs['wid']))
                if not worker:
                    self.response.status = 404
                    self.response.status_message = "Worker Not Found"
                    self.response.write(self.response.status_message)
                    return
            # Remove teh worker from the captian list before removing the worker
            if worker in captian.worker_list:
                count = 0
                w_list = []
                for n in captian.worker_list:
                    if worker != n:
                        w_list.append(n)
                    count += 1
                captian.worker_list = w_list
                captian.put()
                worker.delete()
                self.response.write('Worker ' + kwargs['wid'] + 'removed from captian ' + kwargs['cid'])

class CaptBoats(webapp2.RequestHandler):
    def put(self, **kwargs):
        if 'application/json' not in self.request.accept:
            self.response.status = 406
            self.response.status_message = "Not Acceptable, Only supports JSON"
            self.response.write(self.response.status_message)
            return
        if 'cid' in kwargs:
            captian = ndb.Key(db_models.Captian, int(kwargs['cid'])).get()
            if not captian:
                self.response.status = 404
                self.response.status_message = "Captian Not Found."
                self.response.write(self.response.status_message)
                return
            if 'bid' in kwargs:
                boat = ndb.Key(db_models.Worker, int(kwargs['bid']))
                if not boat:
                    self.response.status = 404
                    self.response.status_message = "Boat Not Found"
                    self.response.write(self.response.status_message)
                    return
            if boat not in captian.boat_list:
                captian.boat_list.append(boat)
                captian.put()
            else:
                self.response.status = 404
                self.response.status_message = "No Worker Duplicates"
                self.response.write(self.response.status_message)
                return
            self.response.write(json.dumps(captian.to_dict()))
            return

    # Remove a worker from the captian
    def delete(self, **kwargs):
        if 'application/json' not in self.request.accept:
            self.response.status = 406
            self.response.status_message = "Not Acceptable, Only supports JSON"
            self.response.write(self.response.status_message)
            return
        if 'cid' in kwargs:
            captian = ndb.Key(db_models.Captian, int(kwargs['cid'])).get()
            if not captian:
                self.response.status = 404
                self.response.status_message = "Captian Not Found."
                self.response.write(self.response.status_message)
                return
            if 'bid' in kwargs:
                boat = ndb.Key(db_models.Boat, int(kwargs['bid']))
                if not boat:
                    self.response.status = 404
                    self.response.status_message = "Boat Not Found"
                    self.response.write(self.response.status_message)
                    return
            # Remove teh boat from the captian list before removing the worker
            if boat in captian.boat_list:
                count = 0
                b_list = []
                for k in captian.boat_list:
                    if boat != k:
                        b_list.append(k)
                    count += 1
                captian.boat_list = b_list
                captian.put()
                boat.delete()
                self.response.write('Boat ' + kwargs['bid'] + 'removed from captian ' + kwargs['cid'])

