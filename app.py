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
from sqlalchemy import create_engine, func, inspect
import pymysql
from Lesly_scrape import compare
import threading
from flask import Flask, jsonify, render_template
import json
import requests


#################################################
# Database Setup
#################################################

if os.environ.get("JAWSDB_URL"):
    connection = os.environ["JAWSDB_URL"]
else:
    from config import connection
engine = create_engine(connection)
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

@app.before_first_request
def activate_job():
    def run_job():
        while True:
            print("Running task")
            compare()
            time.sleep(21600)

    thread = threading.Thread(target=run_job)
    thread.start()

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
    return jsonify(json.loads(new_home))

def start_runner():
    def start_loop():
        has_started = False
        while not has_started:
            try:
                r = requests.get("https://county-flood-control.herokuapp.com:33507/") 
                if r.status_code == 200:
                    print("server started")
                    has_started = True
                print(r.status_code)
            except: 
                print("ex")
            time.sleep(21600)
    thread = threading.Thread(target=start_loop)
    thread.start()


if __name__ == "__main__":
    app.debug = False
    start_runner()
    app.run()
