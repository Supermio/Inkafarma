
import os
from google.appengine.ext import db
import cgi
import urllib
from datetime import datetime
from models import models
import webapp2
from google.appengine.ext.webapp import template
import getData

class MainHandler(webapp2.RequestHandler):
   def get(self):
      template_values = {
         'title'  : 'supertitulo',
         'year'   : datetime.now().strftime("%Y"),
         'domain' : 'superdominio'
         }
      path = "views/default.html"
      self.response.out.write(template.render(path, template_values))

   def post(self):
      pcodEmpleado= self.request.get('pcodEmpleado')
      pDia = self.request.get('pdia')
      pMes = self.request.get('pmes')
      pAno = self.request.get('pano')
      pfechaNac =  pDia +"/"+pMes+ "/"+ pAno ##self.request.get('pfechaNac')
      pnumDoc = self.request.get('pDNI')
      		
      ##tmpEmpleados =db.GqlQuery("Select * from inEmpleado "
      ##                          "where idEmpleado = :1 and "
      ##                          "fechaNac = :2 and "
      ##                          "numDoc = :3",pcodEmpleado, pfechaNac, pnumDoc)
      tmpEmpleados = getData.authenticar(pcodEmpleado,pfechaNac,pnumDoc)
      
      total = tmpEmpleados.count()
      template_values = {'error': 'Ok'}
      
      if total==1:
         pkey= tmpEmpleados[0]
         pEmp = getData.getEmp(pkey)
         path =  "views/main.html"
         template_values = {'emp'    : pEmp,
                            'empkey' : pkey}
      else:
         path = "views/default.html"
         template_values = {"error": "Credenciales invalidas",
                            "total": total}
      
      self.response.out.write(template.render(path, template_values))
   