#!/usr/bin/env python

# Importing the controllers that will handle
# the generation of the pages:
from controllers import login, menu, ubigeo

# Importing some of Google's AppEngine modules:
import webapp2

# This is the main method that maps the URLs
# of your application with controller classes.
# If a URL is requested that is not listed here,
# a 404 error is displayed.


application = webapp2.WSGIApplication([('/', login.MainHandler),
                ('/main.html', menu.MainHandler),
                ('/ubigeo.html', ubigeo.MainHandler)],debug=True)