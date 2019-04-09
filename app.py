#################################################
# Import Dependencies
################################################## 
import os
import time 
import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
#import pymysql

from flask import Flask, jsonify, render_template
#from flask_sqlalchemy import SQLAlchemy




#################################################
# Database Setup
#################################################

engine = os.environ.get("JAWSDB_URL") or create_engine("mysql+pymysql://root:banana@localhost/homes_db")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

print(dir(Base.classes))
print(Base.classes.keys())
print(Base.classes.items())

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


# @app.route("/buyouts/search")
# def search():
#     return render_template("index.html")
    

# @app.route("/buyouts/analytics")
# def analytics():
#     return render_template("index.html")

# @app.route("/buyouts/faqs")
# def faqs():
#     return render_template("index.html")


# @app.route("/buyouts/alerts")
# def alerts():
#     return render_template("index.html")



#@app.route("/buyouts/charts")
#def charts():
    #return render_templates ("")


#@app.route("/buyouts/about")
# def about():
#     return render_template("index.html")



#API routes below here 

#need an api route for search
#single neighborhood

@app.route('/api/neighborhood', defaults={'neighborhood':True})
@app.route("/api/neighborhood/<neighborhood>")
def api(neighborhood):
    print("neighborhood route")
    query = session.query(home_table.Neighborhood,home_table.Address, home_table.Price, home_table.Days_on_Market, home_table.Agent)
    
    if neighborhood == True:
        results = query.all()
    else:
        results = query.filter_by(Address = neighborhood)

    return jsonify(results)
   

#change from array of arrays into an array of objects
#query for a specific neighborhood instead of all rows 




#Neighborhood Name
#Address
#Price
#Days on Market
#Agent    
    

#need an API route for analytics 

# @app.route("/api")
# def dummy():
#     return jsonify({
#         "test": "success"
#     })

if __name__ == "__main__":
    app.run()