# Author: Jeffrey Schachtsick
# CS 496 - Mobile/Cloud Development
# Assignment 2: Dynamic Pages
# Subject: Car Inventory
# File: main.py
# Last Update: 10/2/2016

import webapp2

config = {'default-group':'car-data'}

# application at base_page
application = webapp2.WSGIApplication([
    # Page to be able to update database
    ('/backend', 'backend.Backend'),
    ('/', 'base_page.CarInventory'),
    ('/view', 'view.ViewCar'),
    ('/edit', 'edit.EditCar')
    #('/edit/car', 'edit_car.EditCar')
], debug=True, config=config)