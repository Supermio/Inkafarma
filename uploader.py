from google.appengine.ext import db
from google.appengine.tools import bulkloader
from models import *

class EmpLoader(bulkloader.Loader):
	def __init__(self):
		bulkloader.Loader.__init__(self,'inEmpleado',
		                          [('idCompania',str),
		                           ('idEmpleado',str),
		                           ('apePat',str),
		                           ('apeMat',str),
		                           ('nombres',str),
		                           ('tipoDoc',str),
		                           ('numDoc',str),
		                           ('fechaNac',str)
		                           ])
		
loaders = [EmpLoader]
