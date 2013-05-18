from google.appengine.ext import db
from google.appengine.api import memcache

def authenticar(pcodEmpleado, pfechaNac, pnumDoc):
    tmpEmpleados =db.GqlQuery("Select __key__ from inEmpleado "
                                "where "
                                "idEmpleado = :1 and "
                                "fechaNac = :2 and "
                                "numDoc = :3",pcodEmpleado, pfechaNac, pnumDoc)
    return tmpEmpleados

def getEmp(pkey):
    ##data = memcache.get('emp')
    ##if data is not None:
    ##    return data
    ##else:
        data = db.get(pkey)
    ##    memcache.add("emp", data, 60)
        return data

def getDatosLibres(pCompania,pEmpleado):
    tmpFree = db.GqlQuery("select empCuenta, empAnexo, empCelular, empRPM, empEmail from libres "
                             " where "
                             " idCompania = :1 and "
                             " idEmpleado = :2",pCompania, pEmpleado)
    return tmpFree
def getAllDepends(pCompania,pEmpleado):
    tmpDepends = db.GqlQuery("select apePat, apeMat, nombres, numDoc from dependiente "
                             " where "
                             " idCompania = :1 and "
                             " idEmpleado = :2",pCompania, pEmpleado)
    return tmpDepends

def getAllEstudios(pCompania,pEmpleado):
    tmpEstudios = db.GqlQuery("select descrip, grado, ciclo, periodIni, periodFin from estudio "
                             " where "
                             " idCompania = :1 and "
                             " idEmpleado = :2",pCompania, pEmpleado)
    return tmpEstudios

def getAllCapas(pCompania,pEmpleado):
    tmpCapas = db.GqlQuery("select nombCurso, fechaIni, fechaFin from capacitacion "
                             " where "  
                             " idCompania = :1 and "
                             " idEmpleado = :2",pCompania, pEmpleado)
    return tmpCapas

def getAllExpers(pCompania,pEmpleado):
    tmpExpers = db.GqlQuery("select empresa, rubro, cargo, fechaIni from experiencia"
                             " where "
                             " idCompania = :1 and "
                             " idEmpleado = :2",pCompania, pEmpleado)
    return tmpExpers

def getAllHabiles(pCompania,pEmpleado):
    tmpHabiles = db.GqlQuery("select descrip, idHabilidad, tipoHabilidad, codCalif from habilidades"
                             " where "
                             " idCompania = :1 and "
                             " idEmpleado = :2",pCompania, pEmpleado)
    return tmpHabiles

def getAllHobs(pCompania,pEmpleado):
    tmpExpers = db.GqlQuery("select idHobbie,descrip from hobbie "
                             " where "
                             " idCompania = :1 and "
                             " idEmpleado = :2",pCompania, pEmpleado)
    return tmpExpers

def getAllAreas(pCompania,pEmpleado):
    tmpExpers = db.GqlQuery("select descrip, idGerencia, idDep, idArea, idSeccion from area "
                             " where "
                             " idCompania = :1 and "
                             " idEmpleado = :2",pCompania, pEmpleado)
    return tmpExpers

def getTipoDocs():
    data = memcache.get('tipodocs')
    if data is not None:
        return data
    else:
        data = db.GqlQuery("Select idValor, nombre from listaValores where idTipo = 1 order by idValor")
        memcache.add("tipodocs", data, 60)
        return data
    
def getTipoVia():
    data = memcache.get('tipovias')
    if data is not None:
        return data
    else:
        data = db.GqlQuery("Select idValor, nombre from listaValores where idTipo = 2 order by idValor")
        memcache.add("tipovias", data, 60)
        return data

def getTipoZona():
    data = memcache.get('tipozonas')
    if data is not None:
        return data
    else:
        data = db.GqlQuery("Select idValor, nombre from listaValores where idTipo = 3 order by idValor")
        memcache.add("tipozonas", data, 60)
        return data

def getTipoVinculo():
    data = memcache.get('tipovinculos')
    if data is not None:
        return data
    else:
        data = db.GqlQuery("Select idValor, nombre from listaValores where idTipo = 4 order by idValor")
        memcache.add("tipovinculos", data, 60)
        return data

def getTipoDocSustento():
    data = memcache.get('tipodocsustentos')
    if data is not None:
        return data
    else:
        data = db.GqlQuery("Select idValor, nombre from listaValores where idTipo = 5 order by idValor")
        memcache.add("tipodocsustentos", data, 60)
        return data

def getTipoBajaDep():
    data = memcache.get('tipobajadep')
    if data is not None:
        return data
    else:
        data = db.GqlQuery("Select idValor, nombre from listaValores where idTipo = 6 order by idValor")
        memcache.add("tipobajadep", data, 60)
        return data

def getGrad():
    data = memcache.get('grados')
    if data is not None:
        return data
    else:
        data = db.GqlQuery("Select idValor, nombre from listaValores where idTipo = 7 order by idValor")
        memcache.add("grados", data, 60)
        return data

def getEsp():
    data = memcache.get('espes')
    if data is not None:
        return data
    else:
        data = db.GqlQuery("Select idValor, nombre from listaValores where idTipo = 8 order by idValor")
        memcache.add("espes", data, 60)
        return data
    
def getEspsFilter(pEsp):
    query ="Select nombre from listaValores where idTipo = 8 and idValor = '" + pEsp +"' order by idValor"
    try:
        data = db.GqlQuery(query)
        return data[0].nombre
    except:
        print "Error con pHab:"+ query
        return query
    

def getTipoCapa():
    data = memcache.get('tipocapas')
    if data is not None:
        return data
    else:
        data = db.GqlQuery("Select idValor, nombre from listaValores where idTipo = 9 order by idValor")
        memcache.add("tipocapas", data, 60)
        return data

def getTipoCur():
    data = memcache.get('tipocurs')
    if data is not None:
        return data
    else:
        data = db.GqlQuery("Select idValor, nombre from listaValores where idTipo = 10 order by idValor" )
        memcache.add("tipocurs", data, 60)
        return data

def getCentroEstudios():
    data = memcache.get('cents')
    if data is not None:
        return data
    else:
        data = db.GqlQuery("Select idValor, nombre from listaValores where idTipo = 11 order by idValor")
        memcache.add("cents", data, 60)
        return data

def getHabilidades():
    data = memcache.get('habils')
    if data is not None:
        return data
    else:
        data = db.GqlQuery("Select idValor, nombre from listaValores where idTipo = 12 order by idValor")
        memcache.add("habils", data, 60)
        return data

def getHabsFilter(pHab):
    query ="Select nombre from listaValores where idTipo = 12 and idValor ='" + pHab + "' order by idValor"
    try:
        data = db.GqlQuery(query)
        return data[0].nombre
    except:
        print "Error con pHab:"+ query
        return query

def getTipoHabil():
    data = memcache.get('tipohabils')
    if data is not None:
        return data
    else:
        data = db.GqlQuery("Select idValor, nombre from listaValores where idTipo = 13 order by idValor")
        memcache.add("tipohabils", data, 60)
        return data

def getCalHabil():
    data = memcache.get('calhabils')
    if data is not None:
        return data
    else:
        data = db.GqlQuery("Select idValor, nombre from listaValores where idTipo = 14 order by idValor")
        memcache.add("calhabils", data, 60)
        return data

def getTurnos():
    data = memcache.get('turnos')
    if data is not None:
        return data
    else:
        data = db.GqlQuery("Select idValor, nombre from listaValores where idTipo = 15 order by idValor")
        memcache.add("turnos", data, 60)
        return data

def getHobbies():
    data = memcache.get('hobbies')
    if data is not None:
        return data
    else:
        data = db.GqlQuery("Select idValor, nombre from listaValores where idTipo = 16 order by idValor")
        memcache.add("hobbies", data, 60)
        return data

def getHobFilter(pHob):
    query ="Select nombre from listaValores where idTipo = 16 and idValor='"+pHob+ "' order by idValor"
    try:
        data = db.GqlQuery(query)
        return data[0].nombre
    except:
        print "Error con pHob:"+ query
        return query
    
def getMonedas():
    data = memcache.get('monedas')
    if data is not None:
        return data
    else:
        data = db.GqlQuery("Select idValor, nombre from listaValores where idTipo = 17 order by idValor")
        memcache.add("monedas", data, 60)
        return data

def getSexo():
    data = memcache.get('sexos')
    if data is not None:
        return data
    else:
        data = db.GqlQuery("Select idValor, nombre from listaValores where idTipo = 18 order by idValor")
        memcache.add("sexos", data, 60)
        return data

def getSino():
    data = memcache.get('sino')
    if data is not None:
        return data
    else:
        data = db.GqlQuery("Select idValor, nombre from listaValores where idTipo = 19 order by idValor")
        memcache.add("sino", data, 60)
        return data
    
def getGerencias():
    data = memcache.get('gerencias')
    if data is not None:
        return data
    else:
        data = db.GqlQuery("Select idGer, nombre from organizacion where idDep = '00' and idArea= '00' and idSeccion = '00'")
        memcache.add("gerencias", data, 60)
        return data

def getDepas(pGer):
    data = db.GqlQuery("Select idDep, nombre from organizacion where idGer=:1 and idArea= '00' and idSeccion = '00'",str(pGer))
    return data

def getAreas(pGer,pDep):
    data = db.GqlQuery("Select idArea, nombre from organizacion where idGer=:1 and idDep=:2 and idSeccion='00'",str(pGer),str(pDep))
    return data 

def getSecciones(pGer,pDep,pArea):
    data = db.GqlQuery("Select idSeccion, nombre from organizacion where idGer=:1 and idDep= :2 and idArea= :3",str(pGer), str(pDep),str(pArea))
    return data

def getEmpleadoDatos(pidCompania,pidEmpleado):
    results = db.GqlQuery("select * from empleado where idCompania=:1 and idEmpleado= :2",pidCompania,pidEmpleado)
    return results

def getUbidep():
    data = memcache.get('ubidep')
    if data is not None:
        return data
    else:
        data = db.GqlQuery("Select ubidep, nombre from ubigeo where ubiprov='00' and ubidist= '00'")
        memcache.add("ubidep", data, 60)
        return data

def getUbiprov(ubidep):
    results =db.GqlQuery("Select ubiprov, nombre from ubigeo where ubidep=:1 and ubiprov!='00' and ubidist= '00'",ubidep)
    return results

def getUbidist(ubidep,ubiprov):
    results =db.GqlQuery("Select ubidist, nombre from ubigeo where ubidep=:1 and ubiprov= :2 and ubidist!='00'" ,ubidep, ubiprov)
    return results

def getVivienda(pidCompania,pidEmpleado):
    results = db.GqlQuery("Select vivProp,vivPropOtros,vivMiembros from adicionales where idCompania= :1, and idEmpleado =  :2",str(pidCompania),str(pidEmpleado))
    return results

def getEnfs(pidCompania,pidEmpleado):
    results = db.GqlQuery("Select vacunas,antEnf,antEnf1,antEnf2,antEnf3,antEnf4,antEnf5,antEnf6,antEnf7,antEnf8,antEnf9,antEnf10,antEnfNote,actEnf,actEnf1,actEnf2,actEnf3,actEnf4,actEnf5,actEnf6,actEnf7,actEnf8,actEnf9,actEnf10,actEnfNote,hSalida,hSalidaNote from adicionales where idCompania = :1 and idEmpleado = :2",str(pidCompania),str(pidEmpleado));
    return results