# Author: Jeffrey Schachtsick
# CS 496 - Mobile/Cloud Development
# Assignment 2: Dynamic Pages
# Subject: Car Inventory
# File: base_page.py
# Last Update: 10/2/2016

import webapp2
import os
import jinja2   # jinja.pocoo.org/docs/dev/api/

class CarInventory(webapp2.RequestHandler):

    # Return the alread stored value in cache
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.Environment(
            loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
            extensions=['jinja2.ext.autoescape'],
            autoescape=True
        )

    # Render templates, defaults to empty dic if there are no template dics supplied
    def render(self, template, template_vars={}):
        template = self.jinja2.get_template(template)
        self.response.write(template.render(template_vars))

# Previous working developement
# Using Jinja for the background environment
#JINJA_ENV = jinja2.Environment(
    # HTML located in sibling dir 'templates'
#    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
#    extensions=['jinja2.ext.autoescape'],
#    autoescape=True
#)

# Class to render the Car Inventory page
#class CarInventory(webapp2.RequestHandler):
    # Set template variables
    #template_vars = {}

    #def get(self):
    #    template = JINJA_ENV.get_template('carinventory.html')
    #    self.response.write(template.render())
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write('Car Inventory!!!!')

    # Post method for entering values into form
    #def post(self):
    #    self.template_vars['form_content'] = {}
    #    template = JINJA_ENV.get_template('carinventory.html')
    #    for i in self.request.arguments():
    #        self.template_vars['form_content'][i] = self.request.get(i)
    #    self.response.write(template.render(self.template_vars))

#class CarInventory(webapp2.RequestHandler):

    # Return the alread stored value in cache
    #@webapp2.cached_property
    #def jinja2(self):
    #    return jinja2.Environment(
    #        loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
    #        extensions=['jinja2.ext.autoescape'],
    #        autoescape=True
    #    )

    # Render templates, defaults to empty dic if there are no template dics supplied
    #def render(self, template, template_vars={}):
    #    template = self.jinja2.get_template(template)
    #    self.response.write(template.render(template_vars))

