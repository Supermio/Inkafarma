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

def getCompletos():
   res = contador.query(ndb.AND(contador.sCaps == 1,
                              contador.sDeps == 1,
                              contador.sEmps == 1,
                              contador.sEsts == 1,
                              contador.sExps == 1,
                              contador.sHabs == 1,
                              contador.sHobs == 1))
   return res

def getCompletos():
   res = contador.query(ndb.AND(contador.sCaps == 1,
                              contador.sDeps == 1,
                              contador.sEmps == 1,
                              contador.sEsts == 1,
                              contador.sExps == 1,
                              contador.sHabs == 1,
                              contador.sHobs == 1))
   return res

class MainHandler(webapp2.RequestHandler):
   def get(self):
      totalCompletos = 0
      totalIncompletos = 0
      try:
	temp = getCompletos()
	totalCompletos = temp.count()
      except Exception, err:
	totalCompletos = 0
      try:
	temp = getIncompletos()
	totalIncompletos = temp.count()
      except Exception,err:
	totalIncompletos = 0
      totalUsuarios = totalCompletos + totalIncompletos
      template_values = {
	'totalUsuarios'    : totalUsuarios,
	'totalCompletos'   : totalCompletos,
	'totalIncompletos' : totalIncompletos
      }
      path = "views/total.html"
      self.response.out.write(template.render(path, template_values))

   def post(self):
      pOpcion = self.request.get('pOpcion')
      print "opcion seleccionada: "+ pOpcion
      if pOpcion == "1":
	empin = getIncompletos()
	template_values = {
         'title'  : 'supertitulo',
         'empin'  : empin
         }
	path = "views/listado.html"
      if pOpcion == "2":
	totalCompletos = 0
        totalIncompletos = 0
        try:
	  temp = getCompletos()
	  totalCompletos = temp.count()
        except Exception, err:
	  totalCompletos = 0
        try:
	  temp = getIncompletos()
	  totalIncompletos = temp.count()
        except Exception,err:
	  totalIncompletos = 0
        totalUsuarios = totalCompletos + totalIncompletos
        template_values = {
	  'totalUsuarios'    : totalUsuarios,
	  'totalCompletos'   : totalCompletos,
	  'totalIncompletos' : totalIncompletos
        }
        path = "views/total.html"
      self.response.out.write(template.render(path, template_values))