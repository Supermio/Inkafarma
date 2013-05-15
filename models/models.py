#!/usr/bin/env python

from google.appengine.ext import db

# These classes define the data objects
# that you will be able to store in
# AppEngine's data store.
class libres(db.Model):
	idCompania  = db.StringProperty(required=True, indexed=True)
	idEmpleado  = db.StringProperty(required=True, indexed=True)
	empCuenta   = db.StringProperty()
	empAnexo    = db.StringProperty()
	empCelular  = db.StringProperty()
	empRPM      = db.StringProperty()
	empEmail    = db.StringProperty()
	
class ubigeo(db.Model):
	ubidep = db.StringProperty(required = True, indexed = True)
	ubiprov = db.StringProperty(required = True, indexed = True)
	ubidist = db.StringProperty(required = True, indexed = True)
	nombre = db.StringProperty()
	
	
class listaValores(db.Model):
	idTipo        = db.IntegerProperty(required  = True, indexed = True)
	idValor       = db.StringProperty(required = True, indexed = True)
	nombre        = db.StringProperty()
	descripcion   = db.StringProperty()
	
class inEmpleado(db.Model):
	idCompania    = db.StringProperty(required = True)
	idEmpleado    = db.StringProperty(required = True, indexed = True)
	apePat        = db.StringProperty()
	apeMat        = db.StringProperty()
	nombres       = db.StringProperty()
	tipoDoc       = db.StringProperty()
	numDoc        = db.StringProperty(indexed = True)
	fechaNac      = db.StringProperty(indexed = True)

class empleado(db.Model):
	idCompania    = db.StringProperty(required = True, indexed = True)
	idEmpleado    = db.StringProperty(required = True, indexed = True)
	domtipoVia    = db.StringProperty()
	domnombreVia  = db.StringProperty()
	domtipoZona   = db.StringProperty()
	domnomZona    = db.StringProperty()
	domnumero     = db.StringProperty()
	dominterior   = db.StringProperty()
	domDept       = db.StringProperty()
	domManz       = db.StringProperty()
	domLote       = db.StringProperty()
	domKm         = db.StringProperty()
	domBlock      = db.StringProperty()
	domEtapa      = db.StringProperty()
	domRef        = db.StringProperty()
	domUbiDep     = db.StringProperty()
	domUbiProv    = db.StringProperty()
	domUbiDist    = db.StringProperty()
	domUbiDescrip = db.StringProperty()
	telfFijo      = db.StringProperty()
	telCel        = db.StringProperty()
	pemail        = db.StringProperty()
	contactoEmer  = db.StringProperty()
	contactoTelF  = db.StringProperty()
	contactoTelC  = db.StringProperty()
	trabInterior  = db.StringProperty()
	turno         = db.StringProperty()
	
class dependiente(db.Model):
	idCompania    = db.StringProperty(required = True, indexed = True)
	idEmpleado    = db.StringProperty(required = True, indexed = True)
	tipoDoc       = db.StringProperty()
	numDoc        = db.StringProperty()
	apePat        = db.StringProperty()
	apeMat        = db.StringProperty()
	nombres       = db.StringProperty()
	fechaNac      = db.StringProperty()
	sexo          = db.StringProperty()
	vinculo       = db.StringProperty()
	tipoDocSus    = db.StringProperty()
	numDocSus     = db.StringProperty()
	fechaAlta     = db.StringProperty()
	fechaBaja     = db.StringProperty()
	motivBaja     = db.StringProperty()
	domicProp     = db.StringProperty()
	domtipoVia    = db.StringProperty()
	domnombreVia  = db.StringProperty()
	domtipoZona   = db.StringProperty()
	domnomZona    = db.StringProperty()
	domnumero     = db.StringProperty()
	dominterior   = db.StringProperty()
	domDept       = db.StringProperty()
	domManz       = db.StringProperty()
	domLote       = db.StringProperty()
	domKm         = db.StringProperty()
	domBlock      = db.StringProperty()
	domEtapa      = db.StringProperty()
	domRef        = db.StringProperty()
	domUbiDep     = db.StringProperty()
	domUbiProv    = db.StringProperty()
	domUbiDist    = db.StringProperty()
	domUbiDescrip = db.StringProperty()
	declarado     = db.StringProperty()
	
class estudio(db.Model):
	idCompania    = db.StringProperty(required = True, indexed = True)
	idEmpleado    = db.StringProperty(required = True, indexed = True)
	grado         = db.StringProperty()
	especialidad  = db.StringProperty()
	centEstudio   = db.StringProperty()
	ciclo         = db.StringProperty()
	periodIni     = db.StringProperty()
	periodFin     = db.StringProperty()
	descrip       = db.StringProperty()
	
class capacitacion(db.Model):
	idCompania    = db.StringProperty(required = True, indexed = True)
	idEmpleado    = db.StringProperty(required = True, indexed = True)
	centEstudio   = db.StringProperty()
	tipoCurso     = db.StringProperty()
	nombCurso     = db.StringProperty()
	fechaIni      = db.StringProperty()
	fechaFin      = db.StringProperty()
	duracion      = db.StringProperty()
	duracionHoras = db.StringProperty()
	tipoCapac     = db.StringProperty()
	costo         = db.StringProperty()
	moneda        = db.StringProperty()
	glosa         = db.StringProperty()

class experiencia(db.Model):
	idCompania    = db.StringProperty(required = True, indexed = True)
	idEmpleado    = db.StringProperty(required = True, indexed = True)
	empresa       = db.StringProperty()
	rubro         = db.StringProperty()
	cargo         = db.StringProperty()
	fechaIni      = db.StringProperty()
	fechaFin      = db.StringProperty()
	glosa         = db.StringProperty()
	
class habilidades(db.Model):
	idCompania    = db.StringProperty(required = True, indexed = True)
	idEmpleado    = db.StringProperty(required = True, indexed = True)
	idHabilidad   = db.StringProperty()
	tipoHabilidad = db.StringProperty()
	codCalif      = db.StringProperty()
	descrip       = db.StringProperty()
	
class hobbie(db.Model):
	idCompania    = db.StringProperty(required = True, indexed = True)
	idEmpleado    = db.StringProperty(required = True, indexed = True)
	idHobbie      = db.StringProperty()
	descrip       = db.StringProperty()

class area(db.Model):
	idCompania    = db.StringProperty(required = True, indexed = True)
	idEmpleado    = db.StringProperty(required = True, indexed = True)
	idGerencia    = db.StringProperty()
	idDep         = db.StringProperty()
	idArea        = db.StringProperty()
	idSeccion     = db.StringProperty()
	descrip       = db.StringProperty()
	
class organizacion(db.Model):
	idGer        = db.StringProperty(required = True, indexed = True)
	idDep        = db.StringProperty(required = True, indexed = True)
	idArea       = db.StringProperty(required = True, indexed = True)
	idSeccion    = db.StringProperty(required = True, indexed = True)
	nombre       = db.StringProperty()
	
