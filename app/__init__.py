from ensurepip import bootstrap
from flask import Flask
from flask_bootstrap import Bootstrap
from .config import DevConfig


#Initializing Application
app = Flask(__name__, instance_relative_config = True)

app.config["SECRET_KEY"] = "12345678"

# Setting Up Configuration
app.config.from_object(DevConfig)    
# app.config.from_pyfile('config.py') 

#Initializing Flask Extensions
bootstrap = Bootstrap(app)  



from app import views