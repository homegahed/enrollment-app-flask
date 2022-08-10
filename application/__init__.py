from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
from dash import Dash


from dash import Dash
from werkzeug.middleware.dispatcher import DispatcherMiddleware
# from routes import dash_app1, dash_app2


app = Flask(__name__)
app.config.from_object(Config)


db = MongoEngine()
db.init_app(app)




from application import routes









