from flask import Flask
from os_query_service import OsQueryService

osQueryService = OsQueryService()


def init_api_routes(app):
    if app:
        app.add_url_rule('/api/timestamp/','getTimeStamp', getTimeStamp, methods=['GET'])
        app.add_url_rule('/api/users/','getLoggedUsers', getLoggedUsers, methods=['GET'])
        app.add_url_rule('/api/processes/','getProcesses', getProcesses, methods=['GET'])



def getTimeStamp():
    return osQueryService.getTimeStamp()


def getLoggedUsers():
    return osQueryService.getLoggedUsers()


def getProcesses():
    return osQueryService.getProcesses()


