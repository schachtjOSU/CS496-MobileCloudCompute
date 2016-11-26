#!/usr/bin/env python
# Author: Jeffrey Schachtsick
# CS 496 - Mobile/Cloud Development
# Final Project
# Subject: Fish Captian App
# File: worker.py
# Last Update: 11/16/2016
# source: Week 4 lecture 'API Demo'

# Imports
import webapp2
from google.appengine.ext import ndb
import db_models
import json

class Worker(webapp2.RequestHandler):
    def post(self):
        if 'application/json' not in self.request.accept:
            self.response.status = 406
            self.response.status_message = "Not Acceptable, Only supports JSON"
            self.response.write(self.response.status_message)
            return
        # Create a new worker and get the properties
        new_worker = db_models.Worker()
        worker_name = self.request.get('worker_name', default_value=None)
        worker_city = self.request.get('worker_city', default_value=None)
        worker_state = self.request.get('worker_state', default_value=None)
        worker_take = self.request.get('worker_take', default_value=None)
        # Make sure we hava a worker name, otherwise send an invalid message
        if worker_name:
            new_worker.worker_name = worker_name
        else:
            self.response.status = 400
            self.response.status_message = "Invalid request, Need a pet name"
            self.response.write(self.response.status_message)
        # Input values of worker city, state, and fish take.  These are optional values
        if worker_city:
            new_worker.worker_city = worker_city
        if worker_state:
            new_worker.worker_state = worker_state
        if worker_take:
            new_worker.worker_take = worker_take
        # Save all values into database
        key = new_worker.put()
        # Return the worker to write to display
        out = new_worker.to_dict()
        self.response.write(json.dumps(out))
        return

    def get(self, **kwargs):
        # Client must ask for a application/json representation in Accept header
        if 'application/json' not in self.request.accept:
            self.response.status = 406
            self.response.status_message = "Not Acceptable format, API must be JSON"
            self.response.write(self.response.status_message)
            return
        # if wid after /worker/.  See main
        if 'wid' in kwargs:
            try:
                out = ndb.Key(db_models.Worker, int(kwargs['wid'])).get().to_dict()
            except:
                self.response.write('Worker not found.')
                return
            self.response.write(json.dumps(out))
        else:
            q = db_models.Worker.query()
            keys = q.fetch(keys_only=True)
            results = { 'keys' : [y.id() for y in keys]}
            self.response.write(json.dumps(results))

class WorkerSearch(webapp2.RequestHandler):
    def post(self):
        # Client must ask for an application/json representation in Accept header
        if 'application/json' not in self.request.accept:
            self.response.status = 406
            self.response.status_message = "Not Acceptable format, API must be JSON"
            return
        q = db_models.Worker.query()
        if self.request.get('worker_name', None):
            q = q.filter(db_models.Worker.worker_name == self.request.get('worker_name'))
        keys = q.fetch(keys_only=True)
        results = { 'keys' : [j.id() for j in keys]}
        self.response.write(json.dumps(results))