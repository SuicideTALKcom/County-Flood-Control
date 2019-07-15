#import dependencies and the web scraping code from scrape.py
from sqlalchemy import create_engine
import pymysql
import pandas as pd
import numpy as np 
import time
from datetime import datetime
import json
import os
# from config import connection

def homes_comparison(scraped_homes):
    #create a connection to the sql database 
    if os.environ.get("JAWSDB_URL"):
        connection = os.environ["JAWSDB_URL"]
    else:
        from config import connection


    engine = create_engine(connection, echo=False)
    conn = engine.connect()
    #put the results of the function into a dataframe
    homesdf = pd.DataFrame(scraped_homes)

    #loop thorugh each new df scrape and compare it against the sql database
    # execute_conn = conn.execute(
    for i, house in homesdf.iterrows():
        #read the sql database and take the address column to compare
        retrieved_data = pd.read_sql(f"SELECT address FROM lmib79r99ct0zdgq.homes WHERE address = '{house['address']}'", engine)
        
        #grab the address from the web scrape and  
        #compare if the address exists against the address column in the sql database

        if retrieved_data.empty:
            format_string = "','"
            string = f"INSERT INTO lmib79r99ct0zdgq.homes ({','.join(homesdf.columns)}) VALUES (\'{format_string.join(house.values)}\')"
            print(string)
            pd.read_sql(string,engine)

    conn.close()

    return 













