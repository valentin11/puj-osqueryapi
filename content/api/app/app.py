from flask import Flask
from os_query_service import OsQueryService
from routes import init_api_routes

app = Flask(__name__)
init_api_routes(app)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
