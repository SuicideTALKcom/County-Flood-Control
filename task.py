#import dependencies and the web scraping code from scrape.py
from sqlalchemy import create_engine
import pymysql
import pandas as pd
import matplotlib 
import numpy as np 
import time
from datetime import datetime

def homes_comparison(homes):
    #create a connection to the sql database 
    engine = create_engine("mysql+pymysql://root:banana@localhost/homes_db", echo=False)

    #put the results of the function into a dataframe
    homesdf = pd.DataFrame(homes)

    homesdf['datetime'] = str(datetime.today())

    #loop thorugh each new df scrape and compare it against the sql database
    for i, house in homesdf.iterrows():
        #read the sql database and take the address column to compare 
        retrieved_data = pd.read_sql(f"SELECT Address FROM home WHERE Address = '{house['address']}'", engine)
        #grab the address from the web scrape and  
        #compare if the address exists against the address column in the sql database
        if retrieved_data.empty:
            homesdf.iloc[i].to_sql('home', if_exists = 'append', con=engine)
    return 


















# homes_df.to_sql('home', if_exists = 'append', con=engine)