#import dependencies and the web scraping code from scrape.py
from sqlalchemy import create_engine
import pymysql
import pandas as pd
import matplotlib 
import numpy as np 
import time
from datetime import datetime
from scrape import har_homes

#create a connection to the sql database 
engine = create_engine("mysql+pymysql://root:banana@localhost/homes_db", echo=False)

#call the function and add the results to a variable
house_list = har_homes()

#put the results of the function into a dataframe
homesdf = pd.DataFrame(house_list)

homesdf['datetime'] = pd.to_datetime.today()



#loop thorugh each new df scrape and compare it against the sql database
for i, house in homesdf.iterrows():
    #read the sql database and take the address column to compare 
    retrieved_data = pd.read_sql(f"SELECT Address FROM home WHERE Address = '{house['address']}'", engine)
    #grab the address from the web scrape and  
    #compare if the address exists against the address column in the sql database
    if retrieved_data.empty:
        homesdf.iloc[i].to_sql('home', if_exists = 'append', con=engine)


       

    # if 

# while True:
#     har_homes()




    # time.sleep(86400)








# csv_path = "../Margret/homes3.csv"
# homes_df = pd.read_csv(csv_path)
# homes_df.head()
# homes_df


















# homes_df.to_sql('home', if_exists = 'append', con=engine)