import os
import cgi
import urllib
from datetime import datetime
from models import models
import getData
import putData
import webapp2
from google.appengine.ext.webapp import template

class MainHandler(webapp2.RequestHandler):
   def get(self):
      ubigeo=self.request.get('ubig')
      deps = getData.getUbidep()
      if ubigeo!='':
         dep  = ubigeo[0:2]
         temp = ubigeo[2:]
         prov = temp[0:2]
         temp1 = temp[2:]
         dis= temp1
         provs = getData.getUbiprov(dep)
         dists = getData.getUbidist(dep,prov)
      else:
         dep=deps[0].ubidep
         provs = getData.getUbiprov(dep)
         prov=provs[0].ubiprov
         dists = getData.getUbidist(dep,prov)
         dis='01'
         
      template_values = {
         'datos'   : '1',
         'pDep'    : dep,
         'pProv'   : prov,
         'pDist'   : dis,
         'deps'    : deps,
         'provs'   : provs,
         'dists'   : dists
         }
      path = "views/ubigeo.html"
      self.response.out.write(template.render(path, template_values))

   def post(self):
         pagina= self.request.get('frmName')
         path = "views/ubigeo.html"
         
         opcion =""
         template_values = {'error': opcion}
         if pagina == "ubigeo":
            action = self.request.get('action')
            if action == "Guardar":
               path = "views/ubigeo.html"
               
               ubidep= self.request.get('pDep')
               ubiprov= self.request.get('pProv')
               ubidist= self.request.get('pDist')
               
               ##Grabar Ubigeo y cerrar ventana
               error='Ingreso de datos'
               template_values = {'error'        : error,
                                  'datos'        : '0'}
            elif action=="Dep":
               ubidep= self.request.get('pDep')
               ubiprov= "01"
               ubidist= "01"
               
               deps = getData.getUbidep()
               provs = getData.getUbiprov(ubidep)
               dists = getData.getUbidist(ubidep,ubiprov)
               error='Modificacion de datos'
               template_values = {'datos'       : '1',
                                  'error'       : error,
                                  'deps'        : deps,
                                  'provs'       : provs,
                                  'dists'       : dists,
                                  'pDep'        : ubidep,
                                  'pProv'       : ubiprov,
                                  'pDist'       : ubidist
                                  }
               
            elif action=="Prov":
               ubidep= self.request.get('pDep')
               ubiprov= self.request.get('pProv')
               ubidist= "01"
               
               deps = getData.getUbidep()
               provs = getData.getUbiprov(ubidep)
               dists = getData.getUbidist(ubidep,ubiprov)
               error='Modificacion de datos'
               template_values = {'datos'       : '1',
                                  'error'       : error,
                                  'deps'        : deps,
                                  'provs'       : provs,
                                  'dists'       : dists,
                                  'pDep'        : ubidep,
                                  'pProv'       : ubiprov,
                                  'pDist'       : ubidist
                                  }
         self.response.out.write(template.render(path, template_values))
   