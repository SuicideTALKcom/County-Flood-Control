#################################################
 # Database Setup
################################################## Import Dependencies
import os
import time 
import pandas as pd
import numpy as np
# from config import connection 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import pymysql
from Lesly_scrape import main
import threading
from flask import Flask, jsonify, render_template
import json

#from flask_sqlalchemy import SQLAlchemy




#################################################
# Database Setup
#################################################

if (os.environ.get("JAWSDB_URL")):
    engine = create_engine(os.environ.get("JAWSDB_URL"))
else:
    engine = create_engine("mysql+pymysql://xq5039a54f2ukgye:pzghos28lbhgg711@otwsl2e23jrxcqvx.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/lmib79r99ct0zdgq")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
insp = inspect(engine)
print(insp.get_table_names())
# Save reference to the table
home = Base.classes.homes

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

@app.route("/county")
def county():
    return render_template("county.html")

@app.route("/neighborhoods")
def neighborhoods():
    return render_template("neighborhoods.html")

@app.route("/analytics")
def analytics():
    return render_template("analytics.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/forecasting")
def forecasting():
    return render_template("forecasting.html")

@app.route("/canvas")
def canvas():
    return render_template("canvas.html")

@app.route("/atest")
def atest():
    return render_template("atest.html")

@app.route("/support")
def support():
    return render_template("support.html")

@app.route("/faqs")
def faqs():
    return render_template("faqs.html")

@app.route("/alerts")
def alerts():
    return render_template("alerts.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/charts")
def charts():
    return render_template ("charts.html")

@app.route("/tableau1")
def tableau1():
    return render_template ("tableau1.html")

@app.route("/tableau2")
def tableau2():
    return render_template ("tableau2.html")

@app.route("/tableau3")
def tableau3():
    return render_template ("tableau3.html")

@app.route("/tableau4")
def tableau4():
    return render_template ("tableau4.html")

@app.route("/about")
def about():
    return render_template("about.html")


#API routes below here 

#need an api route for search
#single neighborhood

@app.route('/api/neighborhood', defaults={'neighborhood':True})
@app.route("/api/neighborhood/<neighborhood>")
def api(neighborhood):
    print("neighborhood route")
    query = session.query(home.neighborhood,home.address, home.price, home.days, home.agent,home.state,home.zip,home.office)
    
    if neighborhood == True:
        results = query.all()
    else:
        results = query.filter_by(Address = neighborhood)

    new_home = pd.DataFrame(results).to_json(orient = 'records')
    
    # from pprint import pprint


    # pprint(json.loads(new_home))

    return jsonify(json.loads(new_home))
   

if __name__ == "__main__":
    app.debug = False
    threading.Thread(target=app.run).start()
    while True:
        main()
   
