from flask import Flask
from flask_compress import Compress
import os
app=Flask(__name__)
app.config["SECRET_KEY"]=os.getenv('2a791f2c550436056dce7322650c3025479d84721e16fa250af7c3a6cfee11fb')
compress=Compress(app)
from whatbreed import routes