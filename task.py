#import dependencies and the web scraping code from scrape.py
from sqlalchemy import create_engine
import pymysql
import pandas as pd
import numpy as np 
import time
from datetime import datetime
# from config import connection 

def homes_comparison(homes):
    #create a connection to the sql database 
    engine = create_engine("mysql://xq5039a54f2ukgye:pzghos28lbhgg711@otwsl2e23jrxcqvx.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/lmib79r99ct0zdgq", echo=False)
    conn = engine.connect()
    cur = conn.cursor()
    #put the results of the function into a dataframe
    homesdf = pd.DataFrame(homes)

    #loop thorugh each new df scrape and compare it against the sql database
    for i, house in homesdf.iterrows():
        #read the sql database and take the address column to compare 
        retrieved_data = pd.read_sql(f"SELECT address FROM lmib79r99ct0zdgq WHERE address = '{house['address']}'", engine)
        #grab the address from the web scrape and  
        #compare if the address exists against the address column in the sql database
        if retrieved_data.empty:
            homesdf.iloc[i].to_sql('lmib79r99ct0zdgq', if_exists = 'append', schema= 'online', con=engine)

    cur.execute(f"INSERT INTO lmib79r99ct0zdgq")
    

    conn.commit()
    
    cur.close()

    conn.close()

    return 


















# homes_df.to_sql('home', if_exists = 'append', con=engine)