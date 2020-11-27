from src.api.concentration_value import api as api_concentration_value
from src.api.user import api as api_user
from src.model import db
from flask import Flask
from flask_cors import CORS

app = Flask("app_name")
app.config.from_object("src.config.BaseConfig")


app.register_blueprint(api_user, url_prefix="/api")
app.register_blueprint(api_concentration_value, url_prefix="/api")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
