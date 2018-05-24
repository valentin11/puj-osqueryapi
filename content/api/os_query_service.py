import osquery

class OsQueryService:
    def makeQuery(self, query):
        instance = osquery.SpawnInstance()
        instance.open()
        response = instance.client.query(query)
	return str(response)

    def getTimeStamp(self):
	return self.makeQuery("select timestamp from time")


# Queries a nivel de usuarios.
    def getLoggedUsers(self):
	# return self.makeQuery("select * from logged_in_users")
	return self.makeQuery("SELECT * FROM users")


# Queries a nivel de procesos.
    def getProcesses(self):
	return self.makeQuery("SELECT * FROM processes")


