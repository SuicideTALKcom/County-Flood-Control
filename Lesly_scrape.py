import os
import time
import csv
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from urllib import parse
import re 
from datetime import datetime
import schedule
import threading 
from task import homes_comparison

def har_homes():
    urls = ["https://www.har.com/riverwood-estates/homes-for-sale/2377?sort=listdate+desc",
            "https://www.har.com/forest-shadows/homes-for-sale/4585?sort=listdate+desc",
           "https://www.har.com/aldine-estates/homes-for-sale/1917?sort=listdate+desc",
           "https://www.har.com/greenbranch/homes-for-sale/1921?sort=listdate+desc",
           "https://www.har.com/castlewood/homes-for-sale/2078?sort=listdate+desc",
           "https://www.har.com/bamwood-terrace/homes-for-sale/3693?sort=listdate+desc",
           "https://www.har.com/lynwood-estates/homes-for-sale/5152?sort=listdate+desc",
           "https://www.har.com/parkwood-estates-77032/homes-for-sale/1911?sort=listdate+desc",
            "https://www.har.com/humble-road-place/homes-for-sale/5738?sort=listdate+desc",
            "https://www.har.com/langley-road-place/homes-for-sale/3838?sort=listdate+desc",
            "https://www.har.com/sandbar-estates/homes-for-sale/9033?sort=listdate+desc",
            "https://www.har.com/houston-hot-wells/homes-for-sale/6115?sort=listdate+desc",
            "https://www.har.com/lake-cypress-estates-u_r/homes-for-sale/6010?sort=listdate+desc",
            "https://www.har.com/bammel-forest/homes-for-sale/2893?sort=listdate+desc",
            "https://www.har.com/airline-farms/homes-for-sale/2045?sort=listdate+desc",
            "https://www.har.com/norchester/homes-for-sale/2949?sort=listdate+desc",
            "https://www.har.com/grantwood/homes-for-sale/6022?sort=listdate+desc",
            "https://www.har.com/windwood-extn-u_r/homes-for-sale/6015?sort=listdate+desc",
            "https://www.har.com/coles-crossing/homes-for-sale/6066?sort=listdate+desc",
            "https://www.har.com/woodwind-lakes/homes-for-sale/2113?sort=listdate+desc",
            "https://www.har.com/woodland-trails-west/homes-for-sale/2103?sort=listdate+desc",
            "https://www.har.com/inwood-pines/homes-for-sale/3649?sort=listdate+desc",
            "https://www.har.com/independence-heights/homes-for-sale/1049?sort=listdate+desc",
            "https://www.har.com/langwood/homes-for-sale/3775?sort=listdate+desc",
            "https://www.har.com/kempwood/homes-for-sale/3355?sort=listdate+desc",
            "https://www.har.com/home-owned-estates/homes-for-sale/947?sort=listdate+desc",
            "https://www.har.com/galenapark/realestate/for_sale?sort=listdate+desc",
            "https://www.har.com/braeburn-glen/homes-for-sale/3076?sort=listdate+desc",
            "https://www.har.com/highland-shores/homes-for-sale/9027?sort=listdate+desc",
            "https://www.har.com/san-jacinto-river-estates/homes-for-sale/8074?sort=listdate+desc",
            "https://www.har.com/bliss-meadows/homes-for-sale/7292?sort=listdate+desc",
            "https://www.har.com/bramley/homes-for-sale/7249?sort=listdate+desc",
            "https://www.har.com/crest-haven-estates/homes-for-sale/7290?sort=listdate+desc",
            "https://www.har.com/spenwick-place/homes-for-sale/9397?sort=listdate+desc",
            "https://www.har.com/sagemont/homes-for-sale/3666?sort=listdate+desc"]

    all_homes = []

    #iterate through the urls
    for url in urls:
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        homes = soup.find('div', class_= "prop_list").text
        neighborhood = url.split('/')[3].replace('-',' ')
        home_info = dict()
        home_info ['neighborhood'] = neighborhood

        try:
            all_info = soup.find('div', class_= 'mpi_info') 
            price = soup.find('div', class_= 'mpi_img')
            full_address = all_info.findAll('a', class_= 'address')[0].text
            split_address = full_address.split(',')
            home_info['address']= split_address[0].strip()
            home_info['city']= split_address[1].strip()
            state_zip = split_address[2].split(' ')
            home_info['state'] = state_zip[1].strip()
            home_info['zip'] = state_zip[2].strip()
            home_info['days']= all_info.findAll('span', class_= 'bold')[1].text
            home_info['agent'] = all_info.findAll('a', class_='bold')[0].text
            home_info['office'] = all_info.findAll('a', class_= 'bold')[1].text
            home_info['price']= price.find('div','price').text.replace(',','').replace('$','').strip()
            home_info['datetime']= str(datetime.today())
            all_homes.append(home_info)
        except:
            print("No results given for " + url)
            continue
            
    return all_homes

def compare():
    homes_comparison(har_homes())
    # print("banana")

def threader(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

schedule.every(180).seconds.do(threader, compare)

def main():    
    schedule.run_pending()
    time.sleep(1)



