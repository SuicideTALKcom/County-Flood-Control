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
from sqlalchemy import create_engine, func
#import pymysql

from flask import Flask, jsonify, render_template
#from flask_sqlalchemy import SQLAlchemy




#################################################
# Database Setup
#################################################

if (os.environ.get("JAWSDB_URL")):
    engine = create_engine(os.environ.get("JAWSDB_URL"))
else:
    engine = create_engine("mysql+pymysql://root:banana@localhost/homes_db")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
print(Base.classes)
# Save reference to the table
home = Base.classes.home

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


@app.route("/buyouts/search")
def search():
    return render_template("index.html")
    

@app.route("/buyouts/analytics")
def analytics():
    return render_template("index.html")

@app.route("/buyouts/faqs")
def faqs():
    return render_template("index.html")


@app.route("/buyouts/alerts")
def alerts():
    return render_template("index.html")



@app.route("/buyouts/charts")
def charts():
    return render_template ("index.html")


@app.route("/buyouts/about")
def about():
    return render_template("index.html")



#API routes below here 

#need an api route for search
#single neighborhood

@app.route('/api/neighborhood', defaults={'neighborhood':True})
@app.route("/api/neighborhood/<neighborhood>")
def api(neighborhood):
    print("neighborhood route")
    query = session.query(home.Neighborhood,home.Address, home.Price, home.Days_on_Market, home.Agent)
    
    if neighborhood == True:
        results = query.all()
    else:
        results = query.filter_by(Address = neighborhood)

    new_home = pd.DataFrame(results).to_json(orient = 'records')
    
    # from pprint import pprint
    import json

    # pprint(json.loads(new_home))

    


    return jsonify(json.loads(new_home))
   

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