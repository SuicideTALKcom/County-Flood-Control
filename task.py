#import dependencies and the web scraping code from scrape.py
from sqlalchemy import create_engine
import pymysql
import pandas as pd
import numpy as np 
import time
from datetime import datetime
import json
# from config import connection 

def homes_comparison(scraped_homes):
    #create a connection to the sql database 
    engine = create_engine("mysql+pymysql://xq5039a54f2ukgye:pzghos28lbhgg711@otwsl2e23jrxcqvx.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/lmib79r99ct0zdgq", echo=False)
    conn = engine.connect()
    # cur = conn.cursor()
    #put the results of the function into a dataframe
    homesdf = pd.DataFrame(scraped_homes)
    



    #what happens when the same house is sold within 3 years? homes sold more than once. Compare datestamp and address if datestamp is one year old 
    #append the data anyways 




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
            # homesdf.iloc[i].to_sql('lmib79r99ct0zdgq.homes', if_exists = 'append', schema= 'online', con=conn)
    # )
#     cur.execute(f"INSERT INTO lmib79r99ct0zdgq.homes VALUES homesdf")
    

    # conn.commit()
    
    # cur.close()

    conn.close()

    return 


# with open('scraped_homes.txt', 'r') as output_file:
#     json.load(all_homes, output_file)













