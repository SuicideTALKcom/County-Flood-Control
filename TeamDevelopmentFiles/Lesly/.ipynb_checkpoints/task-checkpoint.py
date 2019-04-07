from sqlalchemy import create_engine
import pymysql
import pandas as pd
import matplotlib 
import numpy as np 

engine = create_engine("mysql+pymysql://root:banana@localhost/homes_db", echo=False)

csv_path = "../Margret/homes3.csv"
homes_df = pd.read_csv(csv_path)
homes_df.head()
homes_df

homes_df.to_sql('home', if_exists = 'append', con=engine)