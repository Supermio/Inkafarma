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
      template_values = {
         'title'  : 'supertitulo',
         'year'   : datetime.now().strftime("%Y"),
         'domain' : 'superdominio'
         }
      
      path = "views/default.html"
      self.response.out.write(template.render(path, template_values))

   def post(self):
         pEmpkey =  self.request.get('empkey')
         pagina= self.request.get('frmName')
         pNavigator = self.request.headers.get('User-Agent')
         path = "views/main.html"
         pEmp = getData.getEmp(pEmpkey)
   
         opcion =""
         template_values = {'error': opcion}
         if pagina == "main":
            opcion = self.request.get('pOpcion')+";"
            
            if opcion == "Salir":
               path="views/default.html"
               template_values={}
               self.redirect("/")
            if opcion == ";":
               path="views/default.html"
               template_values={}
               self.redirect("/")
            opcion = opcion[0]
            if  opcion == "0":
               putData.setDisclaimer(pEmp.idCompania,pEmp.idEmpleado,pNavigator)
               path= "views/main.html"
               template_values = {'emp' : pEmp,
                                    'error': ''}
            if   opcion == "1":
                 path = "views/page000.html"
                 tipovias  = getData.getTipoVia()
                 tipozonas = getData.getTipoZona()
                 turnos    = getData.getTurnos()
                 sino      = getData.getSino()
                 ##if len(pdep) == 0:
                 ##    provs = getData.getUbiprov(tmpDep)
                 ##    error += 'cargando provs de amazonas'
                 ##else:
                 ##    provs = getData.getUbiprov(pdep)
                 ##    error += 'cargando provs de amazonas del post:'+ str(len(pdep))
                 ##if len(pprov) == 0:
                 ##    dists = getData.getUbidist(tmpDep,provs[0].ubiprov)
                 ##    error += 'cargando provs de amazonas y dist'
                 ##else:
                 ##    dists = getData.getUbidist(pdep,pprov)
                 
                 empDatos = getData.getEmpleadoDatos(pEmp.idCompania, pEmp.idEmpleado)
                 if empDatos.count() == 0:
                    error='Ingreso de datos'
                    template_values = {'emp'          : pEmp,
                                       'error'        : error,
                                       'datos'        : '0',
                                       'tipovias'     : tipovias,
                                       'tipozonas'    : tipozonas,
                                       'turnos'       : turnos,
                                       'ubigeo'       : '010101',
                                       'sino'         : sino,
                                       'vivProp'      : '',
                                       'vivPropOtros' : '',
                                       'mMiembros'    : ''}
                 else:
                    error='Modificacion de datos'
                    empViv = getData.getVivienda(pEmp.idCompania, pEmp.idEmpleado)
                    vivProp = '';
                    vivPropOtros = '';
                    mMiembros = '';
                    if empViv.count() > 0:
                       vivProp = empViv[0].vivProp
                       vivPropOtros = empViv[0].vivPropOtros
                       mMiembros = empViv[0].vivMiembros
                    template_values = {'emp'         : pEmp,
                                       'empData'     : empDatos[0],
                                       'datos'       : '1',
                                       'error'       : error,
                                       'tipovias'    : tipovias,
                                       'tipozonas'   : tipozonas,
                                       'turnos'      : turnos,
                                       'sino'        : sino,
                                       'vivProp'     : vivProp,
                                       'vivPropOtros': vivPropOtros,
                                       'mMiembros'   : mMiembros}
            elif opcion == "2":
                 path = "views/page010.html"
                 deps = getData.getAllDepends(pEmp.idCompania,
                                              pEmp.idEmpleado)
                 template_values = {'emp'          : pEmp,
                                    'error'        : opcion,
                                    'dependientes' : deps}
            elif opcion == "3":
                 path = "views/page020.html"
                 estudios = getData.getAllEstudios(pEmp.idCompania,
                                                   pEmp.idEmpleado)
                 template_values = {'emp'       : pEmp,
                                    'error'     : opcion,
                                    'estudios'  : estudios}
            elif opcion == "4":
                 path = "views/page030.html"
                 capacs = getData.getAllCapas(pEmp.idCompania,
                                              pEmp.idEmpleado)
                 template_values = {'emp'       : pEmp,
                                    'error'     : opcion,
                                    'capacs'    : capacs}
            elif opcion =="5":
                 path = "views/page040.html"
                 expers = getData.getAllExpers(pEmp.idCompania,
                                               pEmp.idEmpleado)
                 template_values = {'emp'       : pEmp,
                                    'error'     : opcion,
                                    'expers'    : expers}
            elif opcion == "6":
                 path = "views/page050.html"
                 habiles = getData.getAllHabiles(pEmp.idCompania,
                                                     pEmp.idEmpleado)
                 template_values = {'emp' : pEmp,
                                    'habiles':habiles,
                                    'error': opcion}
            elif opcion == "7":
                 path = "views/page060.html"
                 hobbies = getData.getAllHobs(pEmp.idCompania,
                                                 pEmp.idEmpleado)
                 template_values = {'emp'      : pEmp,
                                    'hobbies'  : hobbies,
                                    'error': opcion}
            elif opcion == "9999":
                 path = "views/page070.html"
                 areas = getData.getAllAreas(pEmp.idCompania,
                                             pEmp.idEmpleado)
                 template_values = {'emp'   : pEmp,
                                    'areas' : areas,
                                    'error' : opcion}
            elif opcion == "8":
                 path = "views/page080.html"
                 libre = getData.getDatosLibres(pEmp.idCompania,
                                          pEmp.idEmpleado)
                 opcion =pEmp.idCompania + '/' + pEmp.idEmpleado
                 cuenta = libre.count();
                 mVac="";
                 antEnf="";
                 antEnf1="";
                 antEnf2="";
                 antEnf3="";
                 antEnf4="";
                 antEnf5="";
                 antEnf6="";
                 antEnf7="";
                 antEnf8="";
                 antEnf9="";
                 antEnf10="";
                 antEnfNote="";
                 actEnf="";
                 actEnf1="";
                 actEnf2="";
                 actEnf3="";
                 actEnf4="";
                 actEnf5="";
                 actEnf6="";
                 actEnf7="";
                 actEnf8="";
                 actEnf9="";
                 actEnf10="";
                 actEnfNote="";
                 hSalida="";
                 hSalidaNote="";
                 if cuenta != 0:
                   cuenta=1
                   enfs = getData.getEnfs(pEmp.idCompania,pEmp.idEmpleado);
                   
                   if enfs.count()>0:
                     mVac        = enfs[0].vacunas;
                     antEnf      = enfs[0].antEnf;
                     antEnf1     = enfs[0].antEnf1;
                     antEnf2     = enfs[0].antEnf2;
                     antEnf3     = enfs[0].antEnf3;
                     antEnf4     = enfs[0].antEnf4;
                     antEnf5     = enfs[0].antEnf5;
                     antEnf6     = enfs[0].antEnf6;
                     antEnf7     = enfs[0].antEnf7;
                     antEnf8     = enfs[0].antEnf8;
                     antEnf9     = enfs[0].antEnf9;
                     antEnf10    = enfs[0].antEnf10;
                     antEnfNote  = enfs[0].antEnfNote;
                     actEnf      = enfs[0].actEnf;
                     actEnf1     = enfs[0].actEnf1;
                     actEnf2     = enfs[0].actEnf2;
                     actEnf3     = enfs[0].actEnf3;
                     actEnf4     = enfs[0].actEnf4;
                     actEnf5     = enfs[0].actEnf5;
                     actEnf6     = enfs[0].actEnf6;
                     actEnf7     = enfs[0].actEnf7;
                     actEnf8     = enfs[0].actEnf8;
                     actEnf9     = enfs[0].actEnf9;
                     actEnf10    = enfs[0].actEnf10;
                     actEnfNote  = enfs[0].actEnfNote;
                     hSalida     = enfs[0].hSalida;
                     hSalidaNote = enfs[0].hSalidaNote;
                 template_values = {'emp'         : pEmp,
                                    'libres'      : libre,
                                    'datos'       : cuenta,
                                    'error'       : opcion,
                                    'mVac'        : mVac,
                                    'antEnf'      : antEnf,
                                    'antEnf1'     : antEnf1,
                                    'antEnf2'     : antEnf2,
                                    'antEnf3'     : antEnf3,
                                    'antEnf4'     : antEnf4,
                                    'antEnf5'     : antEnf5,
                                    'antEnf6'     : antEnf6,
                                    'antEnf7'     : antEnf7,
                                    'antEnf8'     : antEnf8,
                                    'antEnf9'     : antEnf9,
                                    'antEnf10'    : antEnf10,
                                    'antEnfNote'  : antEnfNote,
                                    'actEnf'      : actEnf,
                                    'actEnf1'     : actEnf1,
                                    'actEnf2'     : actEnf2,
                                    'actEnf3'     : actEnf3,
                                    'actEnf4'     : actEnf4,
                                    'actEnf5'     : actEnf5,
                                    'actEnf6'     : actEnf6,
                                    'actEnf7'     : actEnf7,
                                    'actEnf8'     : actEnf8,
                                    'actEnf9'     : actEnf9,
                                    'actEnf10'    : actEnf10,
                                    'actEnfNote'  : actEnfNote,
                                    'hSalida'     : hSalida,
                                    'hSalidaNote' : hSalidaNote}
         elif pagina=="page000":
            action= self.request.get("control")
            path= "views/main.html"
            template_values = {'error': action}
            if   action == "Cancelar" or action == "Regresar":
                 path= "views/main.html"
                 template_values = {'emp' : pEmp,
                                    'error': action}
            elif action=="Guardar":
                 error = self.request.get('pTipoVia')
                 empDatos = getData.getEmpleadoDatos(pEmp.idCompania, pEmp.idEmpleado)
                 tmpubi = str(self.request.get('pubigeo'))
                 if tmpubi=="":
                  pdep=""
                  pprov=""
                  pdist=""
                  pubides=""
                 else:
                  pdep=str(tmpubi[0:2])
                  temp=tmpubi[2:]
                  pprov=str(temp[0:2])
                  temp=temp[2:]
                  pdist=str(temp[0:2])
                  pubides=tmpubi[7:]
                 if empDatos.count() == 0:
                     putData.setEmp(pEmp.idCompania,
                        pEmp.idEmpleado,
                        self.request.get('pTipoVia'),
                        self.request.get('nomVia'),
                        self.request.get('pTipoZona'),
                        self.request.get('pnomZona'),
                        self.request.get('pnum'),
                        self.request.get('pinterior'),
                        self.request.get('pdepartamento'),
                        self.request.get('pmanzana'),
                        self.request.get('plote'),
                        self.request.get('pkm'),
                        self.request.get('pblock'),
                        self.request.get('petapa'),
                        self.request.get('preferencia'),
                        pdep,
                        pprov,
                        pdist,
                        pubides,
                        self.request.get('ptelFijo'),
                        self.request.get('ptelCel'),
                        self.request.get('pemail'),
                        self.request.get('pcontactEmer'),
                        self.request.get('pcontactoTelF'),
                        self.request.get('pcontactoTelC'),
                        self.request.get('ptrabInterior'),
                        self.request.get('pturno')
                        )                
                 else:
                     putData.updEmp(empDatos[0].key(),
                        self.request.get('pTipoVia'),
                        self.request.get('nomVia'),
                        self.request.get('pTipoZona'),
                        self.request.get('pnomZona'),
                        self.request.get('pnum'),
                        self.request.get('pinterior'),
                        self.request.get('pdepartamento'),
                        self.request.get('pmanzana'),
                        self.request.get('plote'),
                        self.request.get('pkm'),
                        self.request.get('pblock'),
                        self.request.get('petapa'),
                        self.request.get('preferencia'),
                        pdep,
                        pprov,
                        pdist,
                        pubides,
                        self.request.get('ptelFijo'),
                        self.request.get('ptelCel'),
                        self.request.get('pemail'),
                        self.request.get('pcontactEmer'),
                        self.request.get('pcontactoTelF'),
                        self.request.get('pcontactoTelC'),
                        self.request.get('ptrabInterior'),
                        self.request.get('pturno')
                        )
                 putData.setVivienda(pEmp.idCompania,
                                     pEmp.idEmpleado,
                                     self.request.get('mViv'),
                                     self.request.get('mVivOtros'),
                                     self.request.get('mMiembros'))
                 path= "views/main.html"
                 template_values = {'emp' : pEmp,
                                    'error': action}
         elif pagina == "page010":
            action= self.request.get("control")
            path= "views/main.html"
            template_values = {'error': action}
            if   action=="Regresar":
                 path= "views/main.html"
                 template_values = {'emp' : pEmp,
                                    'error': action}
            elif action=="Agregar":
                 path = "views/page011.html"
                 tipodocs = getData.getTipoDocs()
                 sexos = getData.getSexo()
                 vinculos = getData.getTipoVinculo()
                 docsus = getData.getTipoDocSustento()
                 motbajas = getData.getTipoBajaDep()
                 sinos = getData.getSino()
                 tipovias  = getData.getTipoVia()
                 tipozonas = getData.getTipoZona()
                 deps = getData.getUbidep()
                 template_values = {'emp'      : pEmp,
                                    'datos'    : '0',
                                    'tipodocs' : tipodocs,
                                    'sexos'    : sexos,
                                    'vinculos' : vinculos,
                                    'docsus'   : docsus,
                                    'motbajas' : motbajas,
                                    'sinos'    : sinos,
                                    'tipovias' : tipovias,
                                    'tipozonas': tipozonas,
                                    'deps'     : deps,
                                    'error'    : self.request.get('pTipoVia')}
            elif action == "Borrar":
               path= "views/page010.html"
               iddep = self.request.get('iddep')
               putData.delRecord(iddep)
               depends = getData.getAllDepends(pEmp.idCompania,
                                              pEmp.idEmpleado)
               template_values = {'emp'             : pEmp,
                                 'dependientes'     : depends,
                                 'error': action}
            elif action=="Editar":
               path= "views/page011.html"
               tipodocs = getData.getTipoDocs()
               sexos = getData.getSexo()
               vinculos = getData.getTipoVinculo()
               docsus = getData.getTipoDocSustento()
               motbajas = getData.getTipoBajaDep()
               sinos = getData.getSino()
               tipovias  = getData.getTipoVia()
               tipozonas = getData.getTipoZona()
               deps = getData.getUbidep()
               
               depend = putData.getDep(self.request.get('iddep'))
               template_values = {'emp'           : pEmp,
                                  'datos'         : '1',
                                  'tipodocs'      : tipodocs,
                                  'sexos'         : sexos,
                                  'vinculos'      : vinculos,
                                  'docsus'        : docsus,
                                  'motbajas'      : motbajas,
                                  'sinos'         : sinos,
                                  'tipovias'      : tipovias,
                                  'tipozonas'     : tipozonas,
                                  'deps'          : deps,
                                  'depend'        : depend,
                                  'error'         : action}
               
         elif pagina == "page020":
            action= self.request.get("control")
            path= "views/main.html"
            template_values = {'error': action}
            if   action=="Regresar":
                 path= "views/main.html"
                 template_values = {'emp' : pEmp,
                                    'error': action}
            elif action=="Agregar":
                 path= "views/page021.html"
                 grados = getData.getGrad()
                 espes = getData.getEsp()
                 cents = getData.getCentroEstudios()
                 template_values = {'emp'     : pEmp,
                                    'datos'   : '0',
                                    'grados'  : grados,
                                    'espes'   : espes,
                                    'cents'   : cents,
                                    'error': action}
            elif action == "Borrar":
               path = "views/page020.html"
               idEst= self.request.get('idest')
               putData.delRecord(idEst)
               estudios = getData.getAllEstudios(pEmp.idCompania,
                                                 pEmp.idEmpleado)
               template_values = {'emp'           : pEmp,
                                  'estudios'      : estudios,
                                  'error'         : action}
            elif action == "Editar":
               path = "views/page021.html"
               grados = getData.getGrad()
               espes = getData.getEsp()
               cents = getData.getCentroEstudios()
               estudio = putData.getDep(self.request.get('idest'))
               template_values = {'emp'     : pEmp,
                                  'datos'   : '1',   
                                  'grados'  : grados,
                                  'espes'   : espes,
                                  'cents'   : cents,
                                  'estudio' : estudio,
                                  'error'   : action}
         elif pagina == "page030":
            action= self.request.get("control")
            path= "views/main.html"
            template_values = {'error': action}
            if   action=="Regresar":
                 path= "views/main.html"
                 template_values = {'emp' : pEmp,
                                    'error': action}
            elif action=="Agregar":
                 path= "views/page031.html"
                 cents = getData.getCentroEstudios()
                 tipoCurs = getData.getTipoCur()
                 tipoCaps = getData.getTipoCapa()
                 monedas = getData.getMonedas()
                 template_values = {'emp'     : pEmp,
                                    'datos'   : '0',
                                    'cents'   : cents,
                                    'tipocurs': tipoCurs,
                                    'tipocaps': tipoCaps,
                                    'monedas' : monedas,
                                    'error': action}
            elif action == "Borrar":
               path = "views/page030.html"
               idCapac= self.request.get('idcapac')
               putData.delRecord(idCapac)
               capacs = getData.getAllCapas(pEmp.idCompania,
                                                 pEmp.idEmpleado)
               template_values = {'emp'           : pEmp,
                                  'capacs'        : capacs,
                                  'error'         : action}
            elif action == "Editar":
               path = "views/page031.html"
               cents = getData.getCentroEstudios()
               tipoCurs = getData.getTipoCur()
               tipoCaps = getData.getTipoCapa()
               monedas = getData.getMonedas()
               
               capac = putData.getDep(self.request.get('idcapac'))
               template_values = {'emp'     : pEmp,
                                  'datos'   : '1',
                                  'cents'   : cents,
                                  'tipocurs': tipoCurs,
                                  'tipocaps': tipoCaps,
                                  'monedas' : monedas,
                                  'capac'   : capac,
                                  'error'   : action}
               
         elif pagina == "page040":
            action= self.request.get("control")
            path= "views/main.html"
            template_values = {'error': action}
            if   action=="Regresar":
                 path= "views/main.html"
                 template_values = {'emp' : pEmp,
                                    'error': action}
            elif action=="Agregar":
                 path= "views/page041.html"
                 template_values = {'emp' : pEmp,
                                    'datos'   : '0',
                                    'error': action}
            elif action== "Borrar":
                 path = "views/page040.html"
                 idexp = self.request.get('idexp')
                 putData.delRecord(idexp)
                 expers = getData.getAllExpers(pEmp.idCompania,
                                               pEmp.idEmpleado)
                 template_values = {'emp'        :pEmp,
                                    'expers'     :expers,
                                    'error'      :opcion}
            elif action == "Editar":
                 path = "views/page041.html"
                 exper = putData.getDep(self.request.get('idexp'))
                 template_values = {'emp'        :pEmp,
                                    'datos'      :'1',
                                    'exper'      :exper,
                                    'error'      :opcion}
         elif pagina == "page050":
            action= self.request.get("control")
            path= "views/main.html"
            template_values = {'error': action}
            if   action=="Regresar":
                 path= "views/main.html"
                 template_values = {'emp' : pEmp,
                                    'error': action}
            elif action=="Agregar":
                 path= "views/page051.html"
                 habs = getData.getHabilidades()
                 tipohabs = getData.getTipoHabil()
                 tipocals = getData.getCalHabil()
                 template_values = {'emp'       : pEmp,
                                    'datos'     : '0',
                                    'habs'      : habs,
                                    'tipohabs'  : tipohabs,
                                    'tipocals'  : tipocals,
                                    'error'     : action}
            elif action == "Borrar":
                 path = "views/page050.html"
                 idhab = self.request.get('idhab')
                 putData.delRecord(idhab)
                 habiles = getData.getAllHabiles(pEmp.idCompania,
                                                 pEmp.idEmpleado)
                 template_values = {'emp'         :pEmp,
                                    'habiles'     :habiles,
                                    'error'       :opcion}
            elif action == "Editar":
                 path = "views/page051.html"
                 habs = getData.getHabilidades()
                 tipohabs = getData.getTipoHabil()
                 tipocals = getData.getCalHabil()
                 
                 hab = putData.getDep(self.request.get('idhab'))
                 template_values = {'emp'        : pEmp,
                                    'datos'      :'1',
                                    'habs'       : habs,
                                    'tipohabs'   : tipohabs,
                                    'tipocals'   : tipocals,
                                    'hab'        : hab,
                                    'error'      : action} 
         elif pagina == "page060":
            action= self.request.get("control")
            path= "views/main.html"
            template_values = {'error': action}
            if   action=="Regresar":
                 path= "views/main.html"
                 template_values = {'emp' : pEmp,
                                    'error': action}
            elif action=="Agregar":
                 path= "views/page061.html"
                 hobbs = getData.getHobbies()
                 template_values = {'emp' : pEmp,
                                    'datos'   : '0',
                                    'hobbies' : hobbs,
                                    'error': action}
            elif action == "Borrar":
                 path= "views/page060.html"
                 idhob = self.request.get('idhob')
                 putData.delRecord(idhob)
                 hobbies = getData.getAllHobs(pEmp.idCompania,
                                              pEmp.idEmpleado)
                 template_values = {'emp'        : pEmp,
                                    'hobbies'    : hobbies,
                                    'error'      : action}
            elif action=="Editar":
               path= "views/page061.html"
               hobbs = getData.getHobbies()
               
               hobbie = putData.getDep(self.request.get('idhob'))
               template_values = {'emp'           : pEmp,
                                  'datos'         : '1',
                                  'hobbies'       : hobbs,
                                  'hobbie'        : hobbie,
                                  'error'         : action}
         elif pagina == "page070":
            action= self.request.get("control")
            path= "views/main.html"
            template_values = {'error': action}
            if   action=="Regresar":
                 path= "views/main.html"
                 template_values = {'emp' : pEmp,
                                    'error': action}
            elif action=="Agregar":
                 path = "views/page071.html"
                 gerencias = getData.getGerencias()
                 departs = getData.getDepas(gerencias[0].idGer)
                 ars = getData.getAreas(gerencias[0].idGer,departs[0].idDep)
                 secs = getData.getSecciones(gerencias[0].idGer,departs[0].idDep,ars[0].idArea)
                 template_values = {'emp'        : pEmp,
                                    'datos'      : '0',
                                    'gerencias'  : gerencias,
                                    'departs'    : departs,
                                    'ars'        : ars,
                                    'secs'       : secs,
                                    'error'      : action}
            elif action == "Borrar":
               path = "views/page070.html"
               idar= self.request.get('idar')
               putData.delRecord(idar)
               areas = getData.getAllAreas(pEmp.idCompania,
                                             pEmp.idEmpleado)
               template_values = {'emp'           : pEmp,
                                  'areas'         : areas,
                                  'error'         : action}
            elif action == "Editar":
               path = "views/page071.html"
               ar = putData.getDep(self.request.get('idar'))
               gerencias = getData.getGerencias()
               departs = getData.getDepas(ar.idGerencia)
               ars = getData.getAreas(ar.idGerencia,ar.idDep)
               secs = getData.getSecciones(ar.idGerencia,ar.idDep,ar.idArea)
               
               template_values = {'emp'         : pEmp,
                                  'datos'       : '1',   
                                  'ar'          : ar,
                                  'gerencias'  : gerencias,
                                  'departs'    : departs,
                                  'ars'        : ars,
                                  'secs'       : secs,
                                  'error'       : action}
         elif pagina=="page080":
            action= self.request.get("control")
            path= "views/page080.html"
            template_values = {'error': action}
            if   action == "Cancelar" or action == "Regresar":
                 path= "views/main.html"
                 template_values = {'emp' : pEmp,
                                    'error': action}
            elif action=="Guardar":
                 datos = self.request.get('datos')
                 error = self.request.get('empkey')
                 libkey = self.request.get('librekey')
                 paso="hola"
                 if datos == "0":
                     putData.setLibres(pEmp.idCompania,
                        pEmp.idEmpleado,
                        self.request.get('cuentared'),
                        self.request.get('anexoempresa'),
                        self.request.get('celularempresa'),
                        self.request.get('rpmempresa'),
                        self.request.get('emailempresa'))
                 else:
                     putData.updLibres(libkey,
                        self.request.get('cuentared'),
                        self.request.get('anexoempresa'),
                        self.request.get('celularempresa'),
                        self.request.get('rpmempresa'),
                        self.request.get('emailempresa'))
                 penf1 = 'False'
                 penf2 = 'False'
                 penf3 = 'False'
                 penf4 = 'False'
                 penf5 = 'False'
                 penf6 = 'False'
                 penf7 = 'False'
                 penf8 = 'False'
                 penf9 = 'False'
                 penf10 = 'False'
                 try:
                     if self.request.get_all('mEnf1')[0] == 'Yes': penf1 = 'True'
                     else: penf1 = 'False'
                 except:
                     penf1 = 'False'
                 try:
                     if self.request.get_all('mEnf2')[0] == 'Yes': penf2 = 'True'
                     else: penf2 = 'False'
                 except:
                     penf2 = 'False'
                 try:
                     if self.request.get_all('mEnf3')[0] == 'Yes': penf3 = 'True'
                     else: penf3 = 'False'
                 except:
                     penf3 = 'False'
                 try:
                     if self.request.get_all('mEnf4')[0] == 'Yes': penf4 = 'True'
                     else: penf4 = 'False'
                 except:
                     penf4 = 'False'
                 try:
                     if self.request.get_all('mEnf5')[0] == 'Yes': penf5 = 'True'
                     else: penf5 = 'False'
                 except:
                     penf5 = 'False'
                 try:
                     if self.request.get_all('mEnf6')[0] == 'Yes': penf6 = 'True'
                     else: penf6 = 'False'
                 except:
                     penf6 = 'False'
                 try:
                     if self.request.get_all('mEnf7')[0] == 'Yes': penf7 = 'True'
                     else: penf7 = 'False'
                 except:
                     penf7 = 'False'
                 try:
                     if self.request.get_all('mEnf8')[0] == 'Yes': penf8 = 'True'
                     else: penf8 = 'False'
                 except:
                     penf8 = 'False'
                 try:
                     if self.request.get_all('mEnf9')[0] == 'Yes': penf9 = 'True'
                     else: penf9 = 'False'
                 except:
                     penf9 = 'False'
                 try:
                     if self.request.get_all('mEnf10')[0] == 'Yes': penf10 = 'True'
                     else: penf10 = 'False'
                 except:
                     penf10 = 'False'
                 penfAct1 = 'False'
                 penfAct2 = 'False'
                 penfAct3 = 'False'
                 penfAct4 = 'False'
                 penfAct5 = 'False'
                 penfAct6 = 'False'
                 penfAct7 = 'False'
                 penfAct8 = 'False'
                 penfAct9 = 'False'
                 penfAct10 = 'False'
                 try:
                     if self.request.get_all('mEnfAct1')[0] == 'Yes': penfAct1 = 'True'
                     else: penfAct1 = 'False'
                 except:
                     penfAct1 = 'False'
                 try:
                     if self.request.get_all('mEnfAct2')[0] == 'Yes': penfAct2 = 'True'
                     else: penfAct2 = 'False'
                 except:
                     penfAct2 = 'False'
                 try:
                     if self.request.get_all('mEnfAct3')[0] == 'Yes': penfAct3 = 'True'
                     else: penfAct3 = 'False'
                 except:
                     penfAct3 = 'False'
                 try:
                     if self.request.get_all('mEnfAct4')[0] == 'Yes': penfAct4 = 'True'
                     else: penfAct4 = 'False'
                 except:
                     penfAct4 = 'False'
                 try:
                     if self.request.get_all('mEnfAct5')[0] == 'Yes': penfAct5 = 'True'
                     else: penfAct5 = 'False'
                 except:
                     penfAct5 = 'False'
                 try:
                     if self.request.get_all('mEnfAct6')[0] == 'Yes': penfAct6 = 'True'
                     else: penfAct6 = 'False'
                 except:
                     penfAct6 = 'False'
                 try:
                     if self.request.get_all('mEnfAct7')[0] == 'Yes': penfAct7 = 'True'
                     else: penfAct7 = 'False'
                 except:
                     penfAct7 = 'False'
                 try:
                     if self.request.get_all('mEnfAct8')[0] == 'Yes': penfAct8 = 'True'
                     else: penfAct8 = 'False'
                 except:
                     penfAct8 = 'False'
                 try:
                     if self.request.get_all('mEnfAct9')[0] == 'Yes': penfAct9 = 'True'
                     else: penfAct9 = 'False'
                 except:
                     penfAct9 = 'False'
                 try:
                     if self.request.get_all('mEnfAct10')[0] == 'Yes': penfAct10 = 'True'
                     else: penfAct10 = 'False'
                 except:
                     penfAct10 = 'False'
                 putData.setEnfes(pEmp.idCompania,
                                  pEmp.idEmpleado,
                                  self.request.get('mVacunas'),
                                  self.request.get('hSalida'),
                                  self.request.get('hSalidaNote'),
                                  self.request.get('mEnf'),
                                  penf1,
                                  penf2,
                                  penf3,
                                  penf4,
                                  penf5,
                                  penf6,
                                  penf7,
                                  penf8,
                                  penf9,
                                  penf10,
                                  self.request.get('mEnfTexto'),
                                  self.request.get('mEnfAct'),
                                  penfAct1,
                                  penfAct2,
                                  penfAct3,
                                  penfAct4,
                                  penfAct5,
                                  penfAct6,
                                  penfAct7,
                                  penfAct8,
                                  penfAct9,
                                  penfAct10,
                                  self.request.get('mEnfActTexto'))
                 path= "views/main.html"
                 template_values = {'emp' : pEmp,
                                    'error': paso}
         elif pagina == "page011":
            action= self.request.get("control")
            path= "views/page010.html"
            template_values = {'error': action}
            if   action=="Cancelar":
                 path= "views/page010.html"
                 deps = getData.getAllDepends(pEmp.idCompania,
                                              pEmp.idEmpleado)
                 template_values = {'emp'          : pEmp,
                                    'error'        : opcion,
                                    'dependientes' : deps}
            elif action=="Guardar":
                 datos = self.request.get('datos')
                 tmpubi = str(self.request.get('pubigeo'))
                 if tmpubi=="":
                  pdep=""
                  pprov=""
                  pdist=""
                  pubides=""
                 else:
                  pdep=str(tmpubi[0:2])
                  temp=tmpubi[2:]
                  pprov=str(temp[0:2])
                  temp=temp[2:]
                  pdist=str(temp[0:2])
                  pubides=tmpubi[7:]
                 pfechaNac= self.request.get('pdiaNac')+"/"+self.request.get('pmesNac')+"/"+self.request.get('panoNac')
                 pfechaAlta= self.request.get('pdiaAlta')+"/"+self.request.get('pmesAlta')+"/"+self.request.get('panoAlta')
                 pfechaBaja= self.request.get('pdiaBaja')+"/"+self.request.get('pmesBaja')+"/"+self.request.get('panoBaja')
                 if datos !="1":
                    putData.setDep(pEmp.idCompania,
                                pEmp.idEmpleado,
                                self.request.get('ptipoDoc'),
                                self.request.get('pnumDoc'),
                                self.request.get('papePat'),
                                self.request.get('papeMat'),
                                self.request.get('pnombres'),
                                pfechaNac,
                                self.request.get('psexo'),
                                self.request.get('pvinculo'),
                                self.request.get('ptipoDocSus'),
                                self.request.get('pnumDocSus'),
                                pfechaAlta,
                                pfechaBaja,
                                self.request.get('pmotivBaja'),
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                self.request.get('pDeclarado'))
                 else:
                    putData.updDep(self.request.get('depkey'),
                                self.request.get('ptipoDoc'),
                                self.request.get('pnumDoc'),
                                self.request.get('papePat'),
                                self.request.get('papeMat'),
                                self.request.get('pnombres'),
                                pfechaNac,
                                self.request.get('psexo'),
                                self.request.get('pvinculo'),
                                self.request.get('ptipoDocSus'),
                                self.request.get('pnumDocSus'),
                                pfechaAlta,
                                pfechaBaja,
                                self.request.get('pmotivBaja'),
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                self.request.get('pDeclarado'))
                     
                 path= "views/page010.html"
                 deps = getData.getAllDepends(pEmp.idCompania,
                                              pEmp.idEmpleado)
                 template_values = {'emp'          : pEmp,
                                    'error'        : 'added',
                                    'dependientes' : deps}
         elif pagina == "page021":
            action= self.request.get("control")
            path= "views/page020.html"
            template_values = {'error': action}
            if   action=="Cancelar":
                 path= "views/page020.html"
                 estudios = getData.getAllEstudios(pEmp.idCompania,
                                                   pEmp.idEmpleado)
                 template_values = {'emp'       : pEmp,
                                    'estudios'  : estudios,
                                    'error'     : action}
            elif action=="Guardar":
                 datos = self.request.get('datos')
                 pperiodoIni = self.request.get('pdiaIni')+"/"+self.request.get('pmesIni')+"/"+self.request.get('panoIni')
                 pperiodoFin = self.request.get('pdiaFin')+"/"+self.request.get('pmesFin')+"/"+self.request.get('panoFin')
                 
                 if datos !="1":
                    putData.setEstudio(pEmp.idCompania,
                                       pEmp.idEmpleado,
                                       self.request.get('pgrado'),
                                       self.request.get('pespecialidad'),
                                       self.request.get('pcentEstudios'),
                                       "",
                                       pperiodoIni,
                                       pperiodoFin)
                 else:
                     putData.updEstudio(self.request.get('estkey'),
                                        self.request.get('pgrado'),
                                        self.request.get('pespecialidad'),
                                        self.request.get('pcentEstudios'),
                                        "",
                                        pperiodoIni,
                                        pperiodoFin)
                     
                 path= "views/page020.html"
                 estudios = getData.getAllEstudios(pEmp.idCompania,
                                                   pEmp.idEmpleado)
                 template_values = {'emp'       : pEmp,
                                    'estudios'  : estudios,
                                    'error'     : action}
         elif pagina == "page031":
            action= self.request.get("control")
            path= "views/page030.html"
            template_values = {'error': action}
            if   action=="Cancelar":
                 path= "views/page030.html"
                 capacs = getData.getAllCapas(pEmp.idCompania,
                                              pEmp.idEmpleado)
                 
                 template_values = {'emp'    : pEmp,
                                    'error'  : action,
                                    'capacs' : capacs}
            elif action=="Guardar":
                 datos = self.request.get('datos')
                 pfechaIni = self.request.get('pdiaIni')+"/"+self.request.get('pmesIni')+"/"+self.request.get('panoIni')
                 pfechaFin = self.request.get('pdiaFin')+"/"+self.request.get('pmesFin')+"/"+self.request.get('panoFin')
                 if datos !="1":
                    putData.setCapac(pEmp.idCompania,
                                     pEmp.idEmpleado,
                                     self.request.get('pcentEstudio'),
                                     self.request.get('pTipoCurso'),
                                     self.request.get('pnomCurso'),
                                     pfechaIni,
                                     pfechaFin,
                                     "",
                                     self.request.get('pDuracionHoras'),
                                     self.request.get('ptipoCapac'),
                                     "",
                                     "",
                                     "")
                 else:
                    putData.updCapac(self.request.get('capkey'),
                                     self.request.get('pcentEstudio'),
                                     self.request.get('pTipoCurso'),
                                     self.request.get('pnomCurso'),
                                     pfechaIni,
                                     pfechaFin,
                                     "",
                                     self.request.get('pDuracionHoras'),
                                     self.request.get('ptipoCapac'),
                                     "",
                                     "",
                                     "")
                 path= "views/page030.html"
                 capacs = getData.getAllCapas(pEmp.idCompania,
                                              pEmp.idEmpleado)
                 template_values = {'emp'     : pEmp,
                                    'capacs'  : capacs,
                                    'error'   : action}
         elif pagina == "page041":
            action= self.request.get("control")
            path= "views/page040.html"
            template_values = {'error': action}
            if   action=="Cancelar":
                 path= "views/page040.html"
                 expers = getData.getAllExpers(pEmp.idCompania,
                                               pEmp.idEmpleado)
                 template_values = {'emp'     : pEmp,
                                    'expers'  : expers,
                                    'error'   : action}
            elif action=="Guardar":
                 datos = self.request.get('datos')
                 pperiodoIni = self.request.get('pdiaIni')+"/"+self.request.get('pmesIni')+"/"+self.request.get('panoIni')
                 pperiodoFin = self.request.get('pdiaFin')+"/"+self.request.get('pmesFin')+"/"+self.request.get('panoFin')
                 if datos !="1":
                    putData.setExper(pEmp.idCompania,
                                     pEmp.idEmpleado,
                                     self.request.get('pempresa'),
                                     self.request.get('prubro'),
                                     self.request.get('pcargo'),
                                     pperiodoIni,
                                     pperiodoFin,
                                     self.request.get('glosa'))
                 else:
                    putData.updExpr(self.request.get('expkey'),
                                    self.request.get('pempresa'),
                                    self.request.get('prubro'),
                                    self.request.get('pcargo'),
                                    pperiodoIni,
                                    pperiodoFin,
                                    self.request.get('pglosa'))
                 path= "views/page040.html"
                 expers = getData.getAllExpers(pEmp.idCompania,
                                               pEmp.idEmpleado)
                 template_values = {'emp'     : pEmp,
                                    'expers'  : expers,
                                    'error'   : action}
         elif pagina == "page051":
            action= self.request.get("control")
            path= "views/page050.html"
            template_values = {'error': action}
            if   action=="Cancelar":
                 path= "views/page050.html"
                 habiles= getData.getAllHabiles(pEmp.idCompania,
                                                pEmp.idEmpleado)
                 template_values = {'emp'      : pEmp,
                                    'habiles'  : habiles,
                                    'error': action}
            elif action=="Guardar":
                 datos = self.request.get('datos')
                 if datos !="1":
                    putData.setHabil(pEmp.idCompania,
                                     pEmp.idEmpleado,
                                     self.request.get('phabilidad'),
                                     "",
                                     self.request.get('ptipocal'))
                 else:
                    putData.updHabil(self.request.get('habkey'),
                                     self.request.get('phabilidad'),
                                     "",
                                     self.request.get('ptipocal'))
                 path= "views/page050.html"
                 habiles = getData.getAllHabiles(pEmp.idCompania,
                                                 pEmp.idEmpleado)
                 template_values = {'emp'      : pEmp,
                                    'habiles'  : habiles,
                                    'error'    : datos}
         elif pagina == "page061":
            action= self.request.get("control")
            path= "views/page060.html"
            template_values = {'error': action}
            if   action=="Cancelar":
                 path= "views/page060.html"
                 hobbies = getData.getAllHobs(pEmp.idCompania,
                                              pEmp.idEmpleado)
                 template_values = {'emp'     : pEmp,
                                    'hobbies' : hobbies,
                                    'error'   : action}
            elif action=="Guardar":
                 datos = self.request.get("datos")
                 newhob = self.request.get('phobbie')
                 if datos =="0":
                    putData.setHobbie(pEmp.idCompania,
                                      pEmp.idEmpleado,
                                      newhob)
                 else:
                    putData.updHobbie(self.request.get('hobkey'),
                                      newhob)
                    
                 path= "views/page060.html"
                 hobbies = getData.getAllHobs(pEmp.idCompania,
                                              pEmp.idEmpleado)
                 template_values = {'emp'     : pEmp,
                                    'hobbies' : hobbies,
                                    'error'   : newhob}
         elif pagina == "page071":
            action= self.request.get("control")
            path= "views/page070.html"
            template_values = {'error': action}
            if   action=="Cancelar":
                 path= "views/page070.html"
                 areas = getData.getAllAreas(pEmp.idCompania,
                                             pEmp.idEmpleado)
                 template_values = {'emp'    : pEmp,
                                    'areas'  : areas,
                                    'error'  : action}
            elif action=="Guardar":
                 datos = self.request.get('datos')
                 arkey = self.request.get('arkey')
                 if arkey=="":
                  datos="0"
                 
                 if datos =="0":
                    putData.setArea(pEmp.idCompania,
                                    pEmp.idEmpleado,
                                    self.request.get('pGerencia'),
                                    self.request.get('pDepart'),
                                    self.request.get('pArea'),
                                    self.request.get('pSeccion'))
                 else:
                    putData.updArea(arkey,
                                    self.request.get('pGerencia'),
                                    self.request.get('pDepart'),
                                    self.request.get('pArea'),
                                    self.request.get('pSeccion'))
                  
                 path= "views/page070.html"
                 areas = getData.getAllAreas(pEmp.idCompania,
                                             pEmp.idEmpleado)
                 template_values = {'emp'     : pEmp,
                                    'areas'   : areas,
                                    'error'   : action}
            elif action=="Ger":
               path = "views/page071.html"
               
               arkey=self.request.get('arkey')
               ar=""
               if arkey !="":
                  ar = putData.getDep(arkey)
               
               pGer = self.request.get('pGerencia')
               pDep = '00'
               pAr = '00'
               pSec = '00'
               
               gerencias = getData.getGerencias()
               departs = getData.getDepas(self.request.get('pGerencia'))
               ars = getData.getAreas(self.request.get('pGerencia'),departs[0].idDep)
               secs = getData.getSecciones(self.request.get('pGerencia'),departs[0].idDep,ars[0].idArea)
               template_values = {'emp'        : pEmp,
                                 'datos'       : '2',
                                 'ar'          : ar,
                                 'gerencias'  : gerencias,
                                 'departs'    : departs,
                                 'ars'        : ars,
                                 'secs'       : secs,
                                 'pGer'       : pGer,
                                 'pDep'       : pDep,
                                 'pAr'        : pAr,
                                 'pSec'       : pSec,
                                 'error'      : action}
            elif action=="Dep":
               path = "views/page071.html"
               
               arkey=self.request.get('arkey')
               ar=""
               if arkey !="":
                  ar = putData.getDep(arkey)
               
               pGer = self.request.get('pGerencia')
               pDep = self.request.get('pDepart')
               pAr = '00'
               pSec = '00'
               
               gerencias = getData.getGerencias()
               departs = getData.getDepas(pGer)
               ars = getData.getAreas(pGer,pDep)
               secs = getData.getSecciones(pGer,pDep,ars[0].idArea)
               
               template_values = {'emp'        : pEmp,
                                 'datos'      : '2',
                                 'ar'         : ar,
                                 'gerencias'  : gerencias,
                                 'departs'    : departs,
                                 'ars'        : ars,
                                 'secs'       : secs,
                                 'pGer'       : pGer,
                                 'pDep'       : pDep,
                                 'pAr'        : pAr,
                                 'pSec'       : pSec,
                                 'error'      : action}
            elif action=="Are":
               path = "views/page071.html"
               
               arkey=self.request.get('arkey')
               ar=""
               if arkey !="":
                  ar = putData.getDep(arkey)
               
               pGer = self.request.get('pGerencia')
               pDep = self.request.get('pDepart')
               pAr = self.request.get('pArea')
               pSec = '00'
               
               gerencias = getData.getGerencias()
               departs = getData.getDepas(self.request.get('pGerencia'))
               ars = getData.getAreas(self.request.get('pGerencia'),self.request.get('pDepart'))
               secs = getData.getSecciones(self.request.get('pGerencia'),self.request.get('pDepart'),self.request.get('pArea'))
               template_values = {'emp'        : pEmp,
                                 'datos'      : '2',
                                 'ar'         : ar,
                                 'gerencias'  : gerencias,
                                 'departs'    : departs,
                                 'ars'        : ars,
                                 'secs'       : secs,
                                 'pGer'       : pGer,
                                 'pDep'       : pDep,
                                 'pAr'        : pAr,
                                 'pSec'       : pSec,
                                 'error'      : action}
         self.response.out.write(template.render(path, template_values))
   