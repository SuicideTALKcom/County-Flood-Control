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
import itertools
import ast
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

    for url in urls:
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'lxml')
        price, homes = itertools.tee(soup.find_all("div", class_="prop_list"))
        neighborhood = url.split('/')[3].replace('-',' ')
        if soup.find_all("h2", {"class":"charcole reguler"}):
            pass

        for item in homes: 
            try:
                for info in item.find_all(class_= 'mpi_info'):
                    full_address = info.find_all('a', class_= 'address')[0].text
                    split_address = full_address.split(',')
                    use_split_address = split_address[0].strip()
                    use_split_city = split_address[1].strip()
                    state_zip = split_address[2].split(' ')
                    use_state = state_zip[1].strip()
                    use_zip = state_zip[2].strip()
                    use_days = info.find_all('span', class_= 'bold')[1].text
                    use_agent = info.find_all('a', class_='bold')[0].text 
                    use_office = info.find_all('a', class_= 'bold')[1].text.strip()

                    home_info=  {
                        "neighborhood": neighborhood,
                        "address": use_split_address,
                        "city": use_split_city,
                        "state": use_state,
                        "zip": use_zip,
                        "days": use_days,
                        "agent": use_agent,
                        "office": use_office}
                    all_homes.append(home_info)


            except:
                print("No results given for " + url)
                continue



        for p in price:
            try:
                for price_div in p.find_all(class_='price'):

                    try:
                        price_div.find('img').decompose()
                    except:
                        print()

                    price_list = price_div.text.replace('$', '').replace(',','').strip('][')


                    new_price = price_list[2:8].strip().split('/n')

                    for new in new_price:
                        final_price = {
                            "price": new
                            }

                    all_homes.append(final_price)

            except:
                print("exception occured")
                continue





    half_len_cities = round(len(all_homes)/2)
    for index in range(half_len_cities):
        all_homes[index]["price"] = all_homes[half_len_cities]["price"]
        del all_homes[half_len_cities]


    print(all_homes)
    return all_homes


def compare():
    homes_comparison(scraped_homes = har_homes())
    # print("banana")

def threader(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

    schedule.every(180).seconds.do(threader, compare)

def main():    
    schedule.run_pending()
    time.sleep(1)



