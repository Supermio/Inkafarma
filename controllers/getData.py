from google.appengine.ext import db
from google.appengine.api import memcache



def authenticar(pcodEmpleado, pfechaNac, pnumDoc):
    tmpEmpleados =db.GqlQuery("Select __key__ from inEmpleado "
                                "where "
                                "idEmpleado = :1 and "
                                "fechaNac = :2 and "
                                "numDoc = :3",pcodEmpleado, pfechaNac, pnumDoc)
    return tmpEmpleados

def getDisclaimer(pcodEmpleado):
    query = "select mAutorizado from autorizado where idEmpleado = :1"
    try:
        data = db.GqlQuery(query,pcodEmpleado)
        return data[0].mAutorizado
    except:
        print "Error con mAutorizado:"+ query
        return "False"
    
def getTextoDis(pCompania,pTexto):
    texto = "<h1><p><strong>Aviso de privacidad de datos para trabajadores de Inkafarma</strong></p></h1><p><strong>El uso de tu informaci&oacute;n personal</strong></p><p>Con el fin de satisfacer sus necesidades, Eckerd Per&uacute; S.A. (InkaFarma), con direcci&oacute;n en Av. Defensores del Morro (ex Huaylas) Nro 1277, Chorrillos, Lima, a trav&eacute;s de su departamento de Gesti&oacute;n Humana, ha preparado el Censo de Colaboradores 2013, mediante el cual se recopilan los siguientes datos personales (i) informaci&oacute;n de car&aacute;cter identificativo como nombres, domicilio, tel&eacute;fonos, correo de contacto; (ii) informaci&oacute;n de car&aacute;cter personal como estado civil, identificaci&oacute;n de personas dependientes, habilidades, pasatiempos, intereses; (iii) informaci&oacute;n de car&aacute;cter laboral como solicitudes de empleo y res&uacute;menes, titulaci&oacute;n acad&eacute;mica y profesional, educaci&oacute;n, empleadores, historial de trabajo, ascensos laborales, capacitaciones, objetivos profesionales, informaci&oacute;n sobre cambios de puestos, renuncias o conclusiones del v&iacute;nculo laboral; e (iv) informaci&oacute;n relativa a la salud como antecedentes de enfermedades.</p><p>El departamento de Gesti&oacute;n Humana usar&aacute; esta informaci&oacute;n para conocer las caracter&iacute;sticas y necesidades del personal de la empresa con el prop&oacute;sito de: (i) identificar a los titulares de beneficios sociales conforme a ley; (ii) ofrecer programas de bienestar social como campa&ntilde;as de vacunaci&oacute;n, habilitaci&oacute;n de nuevas instalaciones, programas de descuentos en productos, programas de cr&eacute;dito, de capacitaci&oacute;n, becas, entre otros beneficios laborales; y (iii) ofrecer incentivos laborales como otorgamiento de d&iacute;as libres, viajes familiares, capacitaciones, cursos, ascensos u obsequios.</p><p>Las preguntas se&ntilde;aladas con un (*) son de respuesta obligatoria. Si elige no completar esta informaci&oacute;n, Inkafarma no podr&aacute; tomarlo en cuenta para sus programas de beneficios, ascensos, capacitaciones, promociones, entre otros de los se&ntilde;alados. Asimismo, la informaci&oacute;n personal suministrada podr&aacute; ser conservada y tratada para los fines antes indicados por el plazo que dure su relaci&oacute;n laboral con Inkafarma.</p><p><strong>Transferencia y almacenamiento de tu informaci&oacute;n personal</strong></p><p>Inkafarma podr&aacute; realizar transferencias nacionales de sus datos personales a otras empresas que formen parte de su grupo econ&oacute;mico y/o empresas con las que comparta programas de beneficios, con el objeto de hacer extensivos los beneficios que dichas empresas otorgan a los trabajadores de InkaFarma.</p><p>Por lo tanto, por el presente documento usted manifiesta su conformidad con que su informaci&oacute;n personal pueda ser almacenada, transferida y sea accesible a otras empresas que formen parte del grupo econ&oacute;mico de InkaFarma y/o empresas con las que comparta programas de beneficios. La informaci&oacute;n personal que suministrar&aacute; ser&aacute; tratada de acuerdo a las leyes de protecci&oacute;n de data personal y privacidad.</p><p><strong>Derechos sobre tu informaci&oacute;n personal</strong></p><p>Usted siempre puede acceder, actualizar y rectificar su informaci&oacute;n personal a trav&eacute;s de Inkafarma, y solicitar su eliminaci&oacute;n cuando termine su v&iacute;nculo laboral con InkaFarma o sus subsidiarias (de ser el caso), pudiendo solicitarlo a trav&eacute;s de cualquier medio escrito, sea esta una carta o un correo electr&oacute;nico dirigido a la Gerencia de Gesti&oacute;n Humana.</p><p><strong>Consentimiento y Autorizaci&oacute;n</strong></p><p>Su consentimiento y autorizaci&oacute;n son requeridos con el fin de continuar con el censo. Si usted est&aacute; de acuerdo, deber&aacute; hacer 'clic' en el bot&oacute;n de 'Aceptar'.</p><p>AL HACER CLIC EN &quot;ACEPTO&quot;, AUTORIZO A INKAFARMA PARA ALMACENAR MI INFORMACI&Oacute;N PERSONAL EN UNA BASE DE DATOS MANTENIDA POR LA EMPRESA QUE PODR&Aacute; ESTAR ALOJADA EN UN SERVIDOR ADMINISTRADO POR GOOGLE INC, Y PARA PROCESAR, TRANSFERIR, USAR, Y DAR TRATAMIENTO DE LA MANERA M&Aacute;S AMPLIA POSIBLE A MI INFORMACI&Oacute;N PERSONAL PARA LOS FINES DESCRITOS EN ESTE AVISO.</p><p><strong>T&eacute;rminos de uso</strong></p><p>Mediante este documento certifico que la informaci&oacute;n que proporciono es verdadera, completa y correcta a mi leal saber y entender. Entiendo que cualquier declaraci&oacute;n falsa, inexactitudes u omisiones hechas por m&iacute; durante el proceso del censo ser&aacute; motivo para que Inkafarma no pueda tomarme en cuenta para sus programas de beneficios, ascensos, capacitaciones, promociones, entre otros de los se&ntilde;alados en este documento, y que podr&iacute;a constituir falta grave.</p><p>Por la presente, autorizo a Inkafarma a verificar, a trav&eacute;s de cualquier medio legal que estime apropiado, cualquier informaci&oacute;n incluida en el presente censo y los hechos resultantes de la verificaci&oacute;n a menos que se indique lo contrario. Reconozco y acepto que Inkafarma podr&aacute; utilizar cualquier informaci&oacute;n obtenida a partir del proceso de verificaci&oacute;n para determinar mi idoneidad para el programa, beneficio, puesto, entre otros, seg&uacute;n lo permitido por la ley aplicable. Yo libero a Inkafarma de cualquier responsabilidad en relaci&oacute;n con este proceso de verificaci&oacute;n.</p>"
    return texto

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
    results = db.GqlQuery("Select vivProp,vivPropOtros,vivMiembros from adicionales where idCompania= :1 and idEmpleado =  :2",str(pidCompania),str(pidEmpleado))
    return results

def getEnfs(pidCompania,pidEmpleado):
    results = db.GqlQuery("Select vacunas,antEnf,antEnf1,antEnf2,antEnf3,antEnf4,antEnf5,antEnf6,antEnf7,antEnf8,antEnf9,antEnf10,antEnfNote,actEnf,actEnf1,actEnf2,actEnf3,actEnf4,actEnf5,actEnf6,actEnf7,actEnf8,actEnf9,actEnf10,actEnfNote,hSalida,hSalidaNote from adicionales where idCompania = :1 and idEmpleado = :2",str(pidCompania),str(pidEmpleado));
    return results