import os
import cgi
import urllib
from datetime import datetime
from models import models
from google.appengine.ext import ndb

import webapp2
from google.appengine.ext.webapp import template

class contador(ndb.Model):
	idCompania   = ndb.StringProperty(required=True, indexed=True)
	idEmpleado   = ndb.StringProperty(required=True, indexed=True)
	nomEmpleado  = ndb.StringProperty()
	mFecha       = ndb.DateTimeProperty(auto_now=True)
	sLibs        = ndb.IntegerProperty()
	sEmps        = ndb.IntegerProperty()
	sDeps        = ndb.IntegerProperty()
	sEsts        = ndb.IntegerProperty()
	sCaps        = ndb.IntegerProperty()
	sExps        = ndb.IntegerProperty()
	sHabs        = ndb.IntegerProperty()
	sHobs        = ndb.IntegerProperty()
	total        = ndb.IntegerProperty()

        
def getIncompletos():
   res = contador.query(ndb.OR(contador.sCaps == 0,
                              contador.sDeps == 0,
                              contador.sEmps == 0,
                              contador.sEsts == 0,
                              contador.sExps == 0,
                              contador.sHabs == 0,
                              contador.sHobs == 0))
   return res

class MainHandler(webapp2.RequestHandler):
   def get(self):
      empin = getIncompletos()
      template_values = {
         'title'  : 'supertitulo',
         'empin'  : empin
         }
      path = "views/listado.html"
      self.response.out.write(template.render(path, template_values))