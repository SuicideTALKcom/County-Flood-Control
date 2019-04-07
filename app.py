
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

engine = create_engine("mysql+pymysql://root:banana@localhost/homes_db")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
home_table = Base.classes.home

# Create our session (link) from Python to the DB
session = Session(engine)



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


@app.route("/search")
def search():
    """Return the list of homes in the database"""

    # Use Pandas to perform the sql query
    stmt = db.session.query(Samples).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])

@app.route("/analytics")



@app.route("/faqs")




@app.route("/about")



@app.route("/api/neighborhood/")
#Send a list of houses in the neighborhood sorted by recency 




if __name__ == "__main__":
    app.run()