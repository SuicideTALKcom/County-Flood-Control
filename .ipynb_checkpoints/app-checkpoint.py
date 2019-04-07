
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
Passenger = Base.classes.passenger

# Create our session (link) from Python to the DB
session = Session(engine)




conn = MySQLdb.connect("mysql+pymysql://root:banana@localhost/homes_db")
cursor = conn.cursor()
def example():
    cursor.execute("select * from name")
    data = cursor.fetchall() #data from database
    return render_template("index.html", value=data)



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
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(Samples).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])






if __name__ == "__main__":
    app.run()