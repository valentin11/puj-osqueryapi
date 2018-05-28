import osquery, os, signal, subprocess32 as subprocess

class OsQueryService:
    def makeQuery(self, query):
        instance = osquery.SpawnInstance()
        instance.open()
        result = instance.client.query(query)
        return result.response

    def runCommand(self, command):
        return os.system(command)

    def killProcess(self, processId):
        try:
            os.kill(processId, signal.SIGKILL)
            return 0
        except OSError:
            return 1



# Queries a nivel de usuarios.
    def getLoggedUsers(self):
	   # return self.makeQuery("select * from logged_in_users")
	   return self.makeQuery("SELECT * FROM users")

    def getLoggedUserById(self, userId):
        return self.makeQuery("SELECT * FROM users WHERE uid = {0}".format(userId))

    def addUser(self, userName, userPass):
    	if self.runCommand("useradd -p {0} {1}".format(userPass, userName)) == 0:
    	    return True
        else:
            return False

    def deleteUser(self, userName):
    	if self.runCommand("deluser {0}".format(userName)) == 0:
    	    return True
        else:
            return False
 


# Queries a nivel de procesos.
    def getProcesses(self):
        return self.makeQuery("SELECT * FROM processes")

    def getProcessById(self, processId):
        return self.makeQuery("SELECT * FROM processes WHERE pid = {0}".format(processId))


    def deleteProcess(self, processId):
        if self.killProcess(processId) == 0:
            return True
        else:
            return False


# Queries a nivel de sistema operativo.
    def getOSVersion(self):
        return self.makeQuery("SELECT version FROM os_version")

    def getKernelVersion(self):
        return self.makeQuery("SELECT version FROM kernel_info")

    def getMemoryCapacity(self):
        return self.makeQuery("SELECT memory_total FROM memory_info")

# Queries a nivel de paquetes instalados.
    def getInstalledPackages(self):
        return self.makeQuery("SELECT * FROM deb_packages")

    def installPackage(self, packageName):
        return self.runCommand("apt-get install -y {0}".format(packageName))

    def removePackage(self, packageName):
        return self.runCommand("apt-get remove -y {0}".format(packageName))