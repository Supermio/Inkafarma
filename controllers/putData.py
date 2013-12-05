from google.appengine.ext import db
from models import models
import getData
import logging

def delRecord(pkey):
    dep = db.get(pkey)
    if not dep is None:
      dep.delete()
      print "Registro borrado"
def getNombres(pidCompania,pidEmpleado):
    query = "select nombres, apePat, apeMat from inEmpleado where idCompania = :1 and idEmpleado = :2"
    try:
        data = db.GqlQuery(query,pidCompania,pidEmpleado)
	nombre = data[0].nombres + " "+data[0].apePat +" "+ data[0].apeMat
	print "Compania:"+pidCompania+" Empleado:"+pidEmpleado+" el nombre es:"+nombre
        return nombre
    except Exception,err:
	print("Error: %s" % err)
        return "John Doe"
def setEmpStatus(pidCompania,pidEmpleado,pidTabla,pStatus):
    sql = "select __key__ from contador where idCompania=:1 and idEmpleado=:2"
    print "Compania:"+pidCompania + " Empleado:"+pidEmpleado
    if pStatus > 0:
	pStatus=1
    try:
        data = db.GqlQuery(sql,pidCompania,pidEmpleado)
        id = data[0]
        data = db.get(id)
        if pidTabla == "libres":
            data.sLibs = pStatus
	    print "actualizare libres"
        if pidTabla == "empleado":
            data.sEmps = pStatus
	    print "actualizare empleado"
        if pidTabla == "dependiente":
            data.sDeps = pStatus
	    print "actualizare dependiente"
        if pidTabla == "estudio":
            data.sEsts = pStatus
	    print "actualizare estudio"
        if pidTabla == "capacitacion":
            data.sCaps = pStatus
	    print "actualizare capacitacion"
        if pidTabla == "experiencia":
            data.sExps = pStatus
	    print "actualizare experiencia"
        if pidTabla == "habilidad":
            data.sHabs = pStatus
	    print "actualizare habilidades"
        if pidTabla == "hobbie":
            data.sHobs = pStatus
	    print "actualizare hobbie"
        data.put()
	print "Registro actualizado con status:"+ str(pStatus)
    except Exception, err:
	print("Error: %s" % err)
        print "Creando Status para este empleado"+pidEmpleado
	sEmps = 0
	sDeps = 0
	sEsts = 0
	sCaps = 0
	sExps = 0
	sHabs = 0
	sHobs = 0
	if pidTabla == "libres":
	    sLibs = pStatus
        if pidTabla == "empleado":
            sEmps = pStatus
        if pidTabla == "dependiente":
            sDeps = pStatus
        if pidTabla == "estudio":
            sEsts = pStatus
        if pidTabla == "capacitacion":
            sCaps = pStatus
        if pidTabla == "experiencia":
            sExps = pStatus
        if pidTabla == "habilidades":
            sHabs = pStatus
        if pidTabla == "hobbie":
            sHobs = pStatus
        e = models.contador(idCompania  = pidCompania,
			    idEmpleado  = pidEmpleado,
			    nomEmpleado = getNombres(pidCompania,pidEmpleado),
			    sEmps       = sEmps,
			    sDeps       = sDeps,
			    sEsts       = sEsts,
			    sCaps       = sCaps,
			    sExps       = sExps,
			    sHabs       = sHabs,
			    sHobs       = sHobs)
	e.put()
	print "Registro creado"

def setDisclaimer(pidCompania,pidEmpleado,pNavegador):
    e = models.autorizado(idCompania  = pidCompania,
                          idEmpleado  = pidEmpleado,
                          mAutorizado = 1,
                          mNavegador  = pNavegador)
    e.put()
def statusLibres(pidCompania,pidEmpleado,pempCuenta, pempAnexo, pempCelular, pempRPM, pempEmail):
    completo = 1
    if pempCuenta == "":
	completo = 0
    if pempAnexo == "":
	completo = 0
    if pempCelular == "":
	completo = 0
    if pempRPM == "":
	completo = 0
    if pempEmail == "":
	completo = 0
    setEmpStatus(pidCompania,pidEmpleado,"libres",completo)    
def setLibres(pidCompania,pidEmpleado,pempCuenta,pempAnexo,pempCelular,pempRPM,pempEmail):
    e = models.libres(idCompania    = pidCompania,
                    idEmpleado       = pidEmpleado,
                    empCuenta        = pempCuenta,
                    empAnexo         = pempAnexo,
                    empCelular       = pempCelular,
                    empRPM           = pempRPM,
                    empEmail         = pempEmail)
    e.put()
    statusLibres(pidCompania,pidEmpleado,pempCuenta,pempAnexo,pempCelular,pempRPM,pempEmail)

def updLibres(pKey, pempCuenta, pempAnexo, pempCelular, pempRPM, pempEmail):
    try:
	e = db.get(pKey)
	e.empCuenta    = pempCuenta
	e.empAnexo     = pempAnexo
	e.empCelular   = pempCelular
	e.empRPM       = pempRPM
	e.empEmail     = pempEmail
	e.put()
	statusLibres(e.idCompania,e.idEmpleado,pempCuenta, pempAnexo, pempCelular, pempRPM, pempEmail)
    except Exception,err:
	print("Error: %s" % err)
    
def setEmp(pidCompania, pidEmpleado,pdomtipovia,pdomnombrevia,pdomtipozona,pdomnomzona,
	pdomnumero,pdominterior,pdomdept,pdommanz,pdomlote,pdomkm,pdomblock,pdometapa,pdomref,pdomubidep,
	pdomubiprov,pdomubidist,pdomubides,ptelffijo,ptelcel,ppemail,pcontactoemer,pcontactotelf,pcontactotelc,
	ptrabinterior,pturno):

    e = models.empleado( idCompania    = pidCompania,
                  idEmpleado    = pidEmpleado,
                  domtipoVia    = pdomtipovia,
                  domnombreVia  = pdomnombrevia,
                  domtipoZona   = pdomtipozona,
                  domnomZona    = pdomnomzona,
                  domnumero     = pdomnumero,
                  dominterior   = pdominterior,
                  domDept       = pdomdept,
                  domManz       = pdommanz,
                  domLote       = pdomlote,
                  domKm         = pdomkm,
                  domBlock      = pdomblock,
                  domEtapa      = pdometapa,
                  domRef        = pdomref,
                  domUbiDep     = pdomubidep,
                  domUbiProv    = pdomubiprov,
                  domUbiDist    = pdomubidist,
                  domUbiDescrip = pdomubides,
                  telfFijo      = ptelffijo,
                  telCel        = ptelcel,
                  pemail        = ppemail,
                  contactoEmer  = pcontactoemer,
                  contactoTelF  = pcontactotelf,
                  contactoTelC  = pcontactotelc,
                  trabInterior  = ptrabinterior,
                  turno         = pturno
                  )
    e.put()
    completo = 1
    if pdomtipovia == "":
	completo = 0
    if pdomnombrevia == "":
	completo = 0
    if pdomtipozona == "":
	completo = 0
    if pdomnomzona == "":
	completo = 0
    if pdomnumero == "":
	completo = 0
    if pdominterior == "":
	completo = 0
    if pdomdept == "":
	completo = 0
    if pdommanz == "":
	completo = 0
    if pdomlote == "":
	completo = 0
    if pdomkm == "":
	completo = 0
    if pdomblock == "":
	completo = 0
    if pdometapa == "":
	completo = 0
    if pdomref == "":
	completo = 0
    if pdomubidep == "":
	completo = 0
    if pdomubiprov == "":
	completo = 0
    if pdomubidist == "":
	completo = 0
    if ptelffijo == "":
	completo = 0
    if ptelcel == "":
	completo = 0
    if ppemail == "":
	completo = 0
    if pcontactoemer == "":
	completo = 0
    if pcontactotelf == "":
	completo = 0
    if pcontactotelc == "":
	completo = 0
    if ptrabinterior == "":
	completo = 0
    if pturno == "":
	completo = 0
    setEmpStatus(pidCompania,pidEmpleado,'empleado',completo)

def updEmp(pKey,pdomtipovia,pdomnombrevia,pdomtipozona,pdomnomzona,
	pdomnumero,pdominterior,pdomdept,pdommanz,pdomlote,pdomkm,pdomblock,pdometapa,pdomref,pdomubidep,
	pdomubiprov,pdomubidist,pdomubides,ptelffijo,ptelcel,ppemail,pcontactoemer,pcontactotelf,pcontactotelc,
	ptrabinterior,pturno):
    try:
	e = db.get(pKey)
	e.domtipoVia    = pdomtipovia
	e.domnombreVia  = pdomnombrevia
	e.domtipoZona   = pdomtipozona
	e.domnomZona    = pdomnomzona
	e.domnumero     = pdomnumero
	e.dominterior   = pdominterior
	e.domDept       = pdomdept
	e.domManz       = pdommanz
	e.domLote       = pdomlote
	e.domKm         = pdomkm
	e.domBlock      = pdomblock
	e.domEtapa      = pdometapa
	e.domRef        = pdomref
	e.domUbiDep     = pdomubidep
	e.domUbiProv    = pdomubiprov
	e.domUbiDist    = pdomubidist
	e.domUbiDescrip = pdomubides
	e.telfFijo      = ptelffijo
	e.telCel        = ptelcel
	e.pemail        = ppemail
	e.contactoEmer  = pcontactoemer
	e.contactoTelF  = pcontactotelf
	e.contactoTelC  = pcontactotelc
	e.trabInterior  = ptrabinterior
	e.turno         = pturno
	
	completo = 1
	if pdomtipovia == "":
	    completo = 0
	if pdomnombrevia == "":
	    completo = 0
	if pdomtipozona == "":
	    completo = 0
	if pdomnomzona == "":
	    completo = 0
	if pdomnumero == "":
	    completo = 0
	if pdominterior == "":
	    completo = 0
	if pdomdept == "":
	    completo = 0
	if pdommanz == "":
	    completo = 0
	if pdomlote == "":
	    completo = 0
	if pdomkm == "":
	    completo = 0
	if pdomblock == "":
	    completo = 0
	if pdometapa == "":
	    completo = 0
	if pdomref == "":
	    completo = 0
	if pdomubidep == "":
	    completo = 0
	if pdomubiprov == "":
	    completo = 0
	if pdomubidist == "":
	    completo = 0
	if ptelffijo == "":
	    completo = 0
	if ptelcel == "":
	    completo = 0
	if ppemail == "":
	    completo = 0
	if pcontactoemer == "":
	    completo = 0
	if pcontactotelf == "":
	    completo = 0
	if pcontactotelc == "":
	    completo = 0
	if ptrabinterior == "":
	    completo = 0
	if pturno == "":
	    completo = 0
	setEmpStatus(e.idCompania,e.idEmpleado,'empleado',completo)
	e.put()
    except Exception, err:
	print("Error: %s" % err)


def setDep(pidCompania,pidEmpleado,ptipoDoc,pnumDoc,papePat,papeMat,pnombres,pfechaNac,psexo,
           pvinculo,ptipoDocSus,pnumDocSus,pfechaAlta,pfechaBaja,pmotivBaja,pdomicProp,
           pdomtipoVia,pdomnombreVia,pdomtipoZona,pdomnomZona,pdomnumero,pdominterior,pdomDept,
           pdomManz,pdomLote,pdomKm,pdomBlock,pdomEtapa,pdomRef,pdomUbiDep,pdomUbiProv,pdomUbiDist,pdomUbides,pdeclarado):

    e = models.dependiente(idCompania    = pidCompania,
               idEmpleado    = pidEmpleado,
               tipoDoc       = ptipoDoc,
               numDoc        = pnumDoc,
               apePat        = papePat,
               apeMat        = papeMat,
               nombres       = pnombres,
               fechaNac      = pfechaNac,
               sexo          = psexo,
               vinculo       = pvinculo,
               tipoDocSus    = ptipoDocSus,
               numDocSus     = pnumDocSus,
               fechaAlta     = pfechaAlta,
               fechaBaja     = pfechaBaja,
               motivBaja     = pmotivBaja,
               domicProp     = pdomicProp,
               domtipoVia    = pdomtipoVia,
               domnombreVia  = pdomnombreVia,
               domtipoZona   = pdomtipoZona,
               domnomZona    = pdomnomZona,
               domnumero     = pdomnumero,
               dominterior   = pdominterior,
               domDept       = pdomDept,
               domManz       = pdomManz,
               domLote       = pdomLote,
               domKm         = pdomKm,
               domBlock      = pdomBlock,
               domEtapa      = pdomEtapa,
               domRef        = pdomRef,
               domUbiDep     = pdomUbiDep,
               domUbiProv    = pdomUbiProv,
               domUbiDist    = pdomUbiDist,
               domUbiDescrip = pdomUbides,
               declarado     = pdeclarado)
    e.put()
    print "voy a actualizar el status"
    setEmpStatus(pidCompania,pidEmpleado,'dependiente',1)
    print "ya actuallice el status"

def updDep(pkey,ptipoDoc,pnumDoc,papePat,papeMat,pnombres,pfechaNac,psexo,
           pvinculo,ptipoDocSus,pnumDocSus,pfechaAlta,pfechaBaja,pmotivBaja,pdomicProp,
           pdomtipoVia,pdomnombreVia,pdomtipoZona,pdomnomZona,pdomnumero,pdominterior,pdomDept,
           pdomManz,pdomLote,pdomKm,pdomBlock,pdomEtapa,pdomRef,pdomUbiDep,pdomUbiProv,pdomUbiDist,pdomUbides,
           pdeclarado):
    try:
	e = db.get(pkey)
	e.tipoDoc       = ptipoDoc
	e.numDoc        = pnumDoc
	e.apePat        = papePat
	e.apeMat        = papeMat
	e.nombres       = pnombres
	e.fechaNac      = pfechaNac
	e.sexo          = psexo
	e.vinculo       = pvinculo
	e.tipoDocSus    = ptipoDocSus
	e.numDocSus     = pnumDocSus
	e.fechaAlta     = pfechaAlta
	e.fechaBaja     = pfechaBaja
	e.motivBaja     = pmotivBaja
	e.domicProp     = pdomicProp
	e.domtipoVia    = pdomtipoVia
	e.domnombreVia  = pdomnombreVia
	e.domtipoZona   = pdomtipoZona
	e.domnomZona    = pdomnomZona
	e.domnumero     = pdomnumero
	e.dominterior   = pdominterior
	e.domDept       = pdomDept
	e.domManz       = pdomManz
	e.domLote       = pdomLote
	e.domKm         = pdomKm
	e.domBlock      = pdomBlock
	e.domEtapa      = pdomEtapa
	e.domRef        = pdomRef
	e.domUbiDep     = pdomUbiDep
	e.domUbiProv    = pdomUbiProv
	e.domUbiDist    = pdomUbiDist
	e.domUbiDescrip = pdomUbides
	e.declarado     = pdeclaradoe.put()
    except Exception, err:
	print("Error: %s" % err)
    
    
def setEstudio(pidCompania,pidEmpleado,pgrado,pespe,pcent,pciclo,pperiodIni,pperiodFin):
    pDescrip = getData.getEspsFilter(pespe)
    e = models.estudio(idCompania    = pidCompania,
                    idEmpleado    = pidEmpleado,
                    grado         = pgrado,
                    especialidad  = pespe,
                    centEstudio   = pcent,
                    ciclo         = pciclo,
                    periodIni     = pperiodIni,
                    periodFin     = pperiodFin,
                    descrip       = pDescrip)
    e.put()


def updEstudio(pkey,pgrado,pespe,pcent,pciclo,pperiodIni,pperiodFin):
    pDescrip = getData.getEspsFilter(pespe)
    try:
	e = db.get(pkey)
	e.grado         = pgrado
	e.especialidad  = pespe
	e.centEstudio   = pcent
	e.ciclo         = pciclo
	e.periodIni     = pperiodIni
	e.periodFin     = pperiodFin
	e.descrip       = pDescrip
	e.put()
    except Exception, err:
	print("Error: %s" % err)

    
def setCapac(pidCompania,pidEmpleado,pcent,ptipoCur,pnomCurso,pfechaIni,pfechaFin,pduracion,
             pduracionhoras,ptipoCapac,pcosto,pmoneda,pglosa):
    e = models.capacitacion(idCompania    = pidCompania,
                    idEmpleado    = pidEmpleado,
                    centEstudio   = pcent,
                    tipoCurso     = ptipoCur,
                    nombCurso     = pnomCurso,
                    fechaIni      = pfechaIni,
                    fechaFin      = pfechaFin,
                    duracion      = pduracion,
                    duracionHoras = pduracionhoras,
                    tipoCapac     = ptipoCapac,
                    costo         = pcosto,
                    moneda        = pmoneda,
                    glosa         = pglosa)
    e.put()

def updCapac(pkey,pcent,ptipoCur,pnomCurso,pfechaIni,pfechaFin,pduracion,
             pduracionhoras,ptipoCapac,pcosto,pmoneda,pglosa):
    try:
	e = db.get(pkey)
	e.centEstudio   = pcent
	e.tipoCurso     = ptipoCur
	e.nombCurso     = pnomCurso
	e.fechaIni      = pfechaIni
	e.fechaFin      = pfechaFin
	e.duracion      = pduracion
	e.duracionHoras = pduracionhoras
	e.tipoCapac     = ptipoCapac
	e.costo         = pcosto
	e.moneda        = pmoneda
	e.glosa         = pglosa
	e.put()
    except Exception, err:
	print("Error: %s" % err)
    

def setExper(pidCompania,pidEmpleado,pEmpresa,prubro,pcargo,pfechaIni,pfechaFin,pglosa):
    e = models.experiencia(idCompania    = pidCompania,
                           idEmpleado    = pidEmpleado,
                           empresa       = pEmpresa,
                           rubro         = prubro,
                           cargo         = pcargo,
                           fechaIni      = pfechaIni,
                           fechaFin      = pfechaFin,
                           glosa         = pglosa)
    e.put()

def updExpr(pkey,pEmpresa,prubro,pcargo,pfechaIni,pfechaFin,pglosa):
    try:
	e = db.get(pkey)
	e.empresa       = pEmpresa
	e.rubro         = prubro
	e.cargo         = pcargo
	e.fechaIni      = pfechaIni
	e.fechaFin      = pfechaFin
	e.glosa         = pglosa
	e.put()
    except Exception, err:
	print("Error: %s" % err)
    
def setHabil(pidCompania,pidEmpleado,pidHabil,ptipoHabil,pcodCalif):
    cuenta=0;
    print "Ya estoy en setHabil"
    try:
        print "Antes de verificar"
        data = db.GqlQuery("select * from habilidades where idHabilidad=:1 and idEmpleado=:2 and idCompania=:3", str(pidHabil),str(pidEmpleado),str(pidCompania))
        cuenta = data.count()
        print "Ya verifique:"+ str(cuenta)
	if cuenta == 0:
	    print "Voy a obtener la descripcion"
	    pDescrip = getData.getHabsFilter(pidHabil)
	    print "Ya tengo la descrip:"+ pDescrip
	    e = models.habilidades(idCompania    = pidCompania,
                           idEmpleado    = pidEmpleado,
                           idHabilidad   = pidHabil,
                           tipoHabilidad = ptipoHabil,
                           codCalif      = pcodCalif,
                           descrip       = pDescrip)
	    e.put()
	    print "Ya grabre la habilidad"
    except Exception,err:
        print("Error: %s" % err)

def updHabil(pkey,pidHabil,ptipoHabil,pcodCalif):
    pDescrip = getData.getHabsFilter(pidHabil)
    try:
	e = db.get(pkey)
	e.idHabilidad   = pidHabil
	e.tipoHabilidad = ptipoHabil
	e.codCalif      = pcodCalif
	e.descrip       = pDescrip
	e.put()
    except Exception, err:
	print("Error: %s" % err)

def setHobbie(pidCompania,pidEmpleado,pidHobbie):
    cuenta=0;
    try:
        data=db.GqlQuery("select * from hobbie where idHobbie=:1 and idEmpleado=:2 and idCompania=:3", str(pidHobbie),str(pidEmpleado),str(pidCompania))
        cuenta= data.count()
        print "Verificando Hobbile"
        if cuenta == 0:
            print "Ya vi que no hay nada"
            pDescrip = getData.getHobFilter(pidHobbie)
            e = models.hobbie(idCompania    = pidCompania,
                          idEmpleado    = pidEmpleado,
                          idHobbie      = pidHobbie,
                          descrip       = pDescrip)
            e.put()
    except Exception,err:
        cuenta=0
        print("Error: %s" % err)


def updHobbie(pkey,pidHobbie):
    pDescrip = getData.getHobFilter(pidHobbie)
    try:
	e = db.get(pkey)
	e.idHobbie   = pidHobbie
	e.descrip    = pDescrip
	e.put() 
    except Exception, err:
	print("Error: %s" % err)

def getGerencia(idGer):
    data=db.GqlQuery("select nombre from organizacion where idGer= :1 and idDep='00' and idArea='00' and idSeccion='00'",str(idGer))
    return data[0].nombre

def getDepartamento(idGer,idDep):
    data=db.GqlQuery("select nombre from organizacion where idGer= :1 and idDep=:2 and idArea='00' and idSeccion='00'",str(idGer),str(idDep))
    return data[0].nombre

def getArea(idGer,idDep,idArea):
    data=db.GqlQuery("select nombre from organizacion where idGer= :1 and idDep=:2 and idArea=:3 and idSeccion='00'",str(idGer),str(idDep),str(idArea))
    return data[0].nombre

def getSec(idGer,idDep,idArea,idSec):
    data=db.GqlQuery("select nombre from organizacion where idGer= :1 and idDep=:2 and idArea=:3 and idSeccion=:4",str(idGer),str(idDep),str(idArea),str(idSec))
    return data[0].nombre


def setArea(pidCompania,pidEmpleado,pidGerencia,pidDep,pidArea,pidSeccion):
    pDescrip = getGerencia(pidGerencia)
    pDescrip = pDescrip + " - " + getDepartamento(pidGerencia,pidDep)
    pDescrip = pDescrip + " - " + getArea(pidGerencia,pidDep,pidArea)
    pDescrip = pDescrip + " - " + getSec(pidGerencia,pidDep,pidArea,pidSeccion)
    
    e = models.area(idCompania    = pidCompania,
                    idEmpleado    = pidEmpleado,
                    idGerencia    = pidGerencia,
                    idDep         = pidDep,
                    idArea        = pidArea,
                    idSeccion     = pidSeccion,
                    descrip       = pDescrip)
    e.put()

def updArea(pkey,pidGerencia,pidDep,pidArea,pidSeccion):
    pDescrip = getGerencia(pidGerencia)
    pDescrip = pDescrip + " - " + getDepartamento(pidGerencia,pidDep)
    pDescrip = pDescrip + " - " + getArea(pidGerencia,pidDep,pidArea)
    pDescrip = pDescrip + " - " + getSec(pidGerencia,pidDep,pidArea,pidSeccion)
    
    e = db.get(pkey)
    e.idGerencia    = pidGerencia
    e.idDep         = pidDep
    e.idArea        = pidArea
    e.idSeccion     = pidSeccion
    e.descrip       = pDescrip
    e.put()
    
def getDep(pkey):
    dep = db.get(pkey)
    return dep

def setVivienda(pidCompania,pidEmpleado,pmViv,pmVivOtros,pmMiembros):
    data = db.GqlQuery("SELECT __key__ from adicionales where idCompania= :1 and idEmpleado= :2",str(pidCompania),str(pidEmpleado))
    total = data.count()
    logging.error('pmViv:'+ pmViv + ' pmVivOtros:'+pmVivOtros +' pmMiembros:' + pmMiembros)
    if total > 0:
       pkey= data[0]
       e = db.get(pkey)
       e.vivProp      = pmViv
       e.vivPropOtros = pmVivOtros
       e.vivMiembros  = pmMiembros
       e.put()
    else:
       e = models.adicionales(idCompania    =  pidCompania,
                              idEmpleado    =  pidEmpleado,
                              vivProp       =  pmViv,
                              vivPropOtros  =  pmVivOtros,
                              vivMiembros   =  pmMiembros)
       e.put()
       
def setEnfes(pidCompania,pidEmpleado,pVac,pmHijosSalida,pmHijosSalidaTexto,pmEnfermedad,pmEnf1,pmEnf2,pmEnf3,pmEnf4,pmEnf5,pmEnf6,pmEnf7,pmEnf8,pmEnf9,pmEnf10,pmEnfTexto,pmEnfActual,pmEnfAct1,pmEnfAct2,pmEnfAct3,pmEnfAct4,pmEnfAct5,pmEnfAct6,pmEnfAct7,pmEnfAct8,pmEnfAct9,pmEnfAct10,pmEnfActTexto):
    data = db.GqlQuery("SELECT __key__ from adicionales where idCompania= :1 and idEmpleado= :2",str(pidCompania),str(pidEmpleado))
    total = data.count()
    if total > 0:
       pkey= data[0]
       e = db.get(pkey)
       e.vacunas       = pVac
       e.hSalida       = pmHijosSalida
       e.hSalidaNote   = pmHijosSalidaTexto
       e.antEnf        = pmEnfermedad
       e.antEnf1       = pmEnf1
       e.antEnf2       = pmEnf2
       e.antEnf3       = pmEnf3
       e.antEnf4       = pmEnf4
       e.antEnf5       = pmEnf5
       e.antEnf6       = pmEnf6
       e.antEnf7       = pmEnf7
       e.antEnf8       = pmEnf8
       e.antEnf9       = pmEnf9
       e.antEnf10      = pmEnf10
       e.antEnfNote    = pmEnfTexto
       e.actEnf        = pmEnfActual
       e.actEnf1       = pmEnfAct1
       e.actEnf2       = pmEnfAct2
       e.actEnf3       = pmEnfAct3
       e.actEnf4       = pmEnfAct4
       e.actEnf5       = pmEnfAct5
       e.actEnf6       = pmEnfAct6
       e.actEnf7       = pmEnfAct7
       e.actEnf8       = pmEnfAct8
       e.actEnf9       = pmEnfAct9
       e.actEnf10      = pmEnfAct10
       e.actEnfNote    = pmEnfActTexto
       e.put()
    else:
       e = models.adicionales(idCompania      =  pidCompania,
                              idEmpleado      =  pidEmpleado,
                              hSalida         =  pmHijosSalida,
                              hSalidaTexto    =  pmHijosSalidaTexto,
                              antEnf          =  pmEnfermedad,
                              antEnf1         =  pmEnf1,
                              antEnf2         =  pmEnf2,
                              antEnf3         =  pmEnf3,
                              antEnf4         =  pmEnf4,
                              antEnf5         =  pmEnf5,
                              antEnf6         =  pmEnf6,
                              antEnf7         =  pmEnf7,
                              antEnf8         =  pmEnf8,
                              antEnf9         =  pmEnf9,
                              antEnf10        =  pmEnf10,
                              antEnfNote      =  pmEnfTexto,
                              actEnf          =  pmEnfActual,
                              actEnf1         =  pmEnfAct1,
                              actEnf2         =  pmEnfAct2,
                              actEnf3         =  pmEnfAct3,
                              actEnf4         =  pmEnfAct4,
                              actEnf5         =  pmEnfAct5,
                              actEnf6         =  pmEnfAct6,
                              actEnf7         =  pmEnfAct7,
                              actEnf8         =  pmEnfAct8,
                              actEnf9         =  pmEnfAct9,
                              actEnf10        =  pmEnfAct10,
                              actEnfNote      =  pmEnfActTexto)
       e.put()