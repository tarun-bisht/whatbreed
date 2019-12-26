from flask import Flask
from flask_compress import Compress
import os
app=Flask(__name__)
app.config["SECRET_KEY"]=os.getenv('SECRET_KEY')
compress=Compress(app)
from whatbreed import routes