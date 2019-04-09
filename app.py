
#################################################
# Database Setup
################################################## Import Dependencies
import os
import time 
import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import pymysql

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy




#################################################
# Database Setup
#################################################




#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")






if __name__ == "__main__":
    app.run()