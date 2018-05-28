from flask import Flask, make_response, request, jsonify
from os_query_service import OsQueryService

osQueryService = OsQueryService()


def init_api_routes(app):
    if app:
        app.add_url_rule('/api/users/','getLoggedUsers', getLoggedUsers, methods=['GET'])
        app.add_url_rule('/api/users/<string:userId>','getLoggedUserById', getLoggedUserById, methods=['GET'])
        app.add_url_rule('/api/users/','addUser', addUser, methods=['POST'])
        app.add_url_rule('/api/users/<string:userName>','deleteUser', deleteUser, methods=['DELETE'])
        app.add_url_rule('/api/processes/','getProcesses', getProcesses, methods=['GET'])
        app.add_url_rule('/api/processes/<string:processId>','getProcessById', getProcessById, methods=['GET'])
        app.add_url_rule('/api/processes/<int:processId>','deleteProcess', deleteProcess, methods=['DELETE'])
        app.add_url_rule('/api/os/','getOSVersion', getOSVersion, methods=['GET'])
        app.add_url_rule('/api/kernel/','getKernelVersion', getKernelVersion, methods=['GET'])
        app.add_url_rule('/api/memory/','getMemoryCapacity', getMemoryCapacity, methods=['GET'])
        app.add_url_rule('/api/packages/','getInstalledPackages', getInstalledPackages, methods=['GET'])
        app.add_url_rule('/api/packages/<string:packageName>','installPackage', installPackage, methods=['POST'])
        app.add_url_rule('/api/packages/<string:packageName>','removePackage', removePackage, methods=['DELETE'])



#Funciones a nivel usuarios
def getLoggedUsers():
    return jsonify({"users": osQueryService.getLoggedUsers()})

def getLoggedUserById(userId):
    return jsonify({"users": osQueryService.getLoggedUserById(userId)})

def addUser():
    jsonBody = request.get_json(force=True)
    if osQueryService.addUser(jsonBody['userName'], jsonBody['userPass']):
        return make_response("Se creo el usuario exitosamente.", 200)
    else:
        return make_response("Error: No se pudo crear el usuario {0}.".format(jsonBody['userName']), 401)

def deleteUser(userName):
    if osQueryService.deleteUser(userName):
        return make_response("Se elimino el usuario exitosamente.", 200)
    else:
        return make_response("Error: No se pudo eliminar el usuario {0}.".format(userName), 401)

#Funciones a nivel prcoesos
def getProcesses():
    return jsonify({"processes": osQueryService.getProcesses()})

def getProcessById(processId):
    return jsonify({"processes": osQueryService.getProcessById(processId)})

def deleteProcess(processId):
    #return make_response("Uid: " + str(os.geteuid()) , 200)
    if osQueryService.deleteProcess(processId):
        return make_response("Se elimino el el proceso exitosamente.", 200)
    else:
        return make_response("Error: No se pudo eliminar el el proceso {0}.".format(processId), 401)

#Funciones a nivel sistema operativo
def getOSVersion():
    return jsonify({"os_version": osQueryService.getOSVersion()})

def getKernelVersion():
    return jsonify({"kernel_version": osQueryService.getKernelVersion()})

def getMemoryCapacity():
    return jsonify({"memory": osQueryService.getMemoryCapacity()})

#Funciones a nivel paquetes
def getInstalledPackages():
    return jsonify({"installed_packages": osQueryService.getInstalledPackages()})

def installPackage(packageName):
    if osQueryService.installPackage(packageName)==0:
        return make_response("Se instalo el paquete exitosamente.", 200)
    else:
        return make_response("Error: No se pudo instalar el paquete {0}.".format(packageName), 401)

def removePackage(packageName):
    if osQueryService.removePackage(packageName)==0:
        return make_response("Se desinstalo el paquete exitosamente.", 200)
    else:
        return make_response("Error: No se pudo desinstalar el paquete {0}.".format(packageName), 401)