import csv
import requests
from bs4 import BeautifulSoup
from pprint import pprint

from urllib import parse
import json
import pandas as pd

urls = ["https://www.har.com/mapsearch/?subdivisions=NorthWest+Park+place&region_id=1&for_sale=1",
        "https://www.har.com/mapsearch/?subdivisions=lismore+lake+estates&for_sale=1",
       "https://www.har.com/mapsearch/?subdivisions=lakewood+oaks+estates&region_id=1&for_sale=1",
       "https://www.har.com/mapsearch/?subdivisions=Riata+West&region_id=1&for_sale=1",
       "https://www.har.com/mapsearch/?subdivisions=Saddle+Ridge+Estates&region_id=1&for_sale=1"]

all_homes = []

for index,url in enumerate(urls):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    homes = soup.findAll('div', {"class": "map_prop_item pointer"})
    neighborhood = dict(parse.parse_qsl(parse.urlsplit(url).query))
    home_info = dict()
    home_info['home_url'] = homes
    home_info['neighborhood'] = neighborhood    
    all_homes.append(home_info)

resultset = []

# for homes in all_homes:
for homes in all_homes:
    for home in homes['home_url']:
        home_details = dict()
        home_details['address'] = home.find('div', {'class': 'mpi_info'}).text.strip('\n\r\t": ').strip('\n\r\t": ').strip('\n\r\t": ').split('\n')[0]
        home_details['price'] = home.find('div', {'class': 'price'}).text.strip('\n\r\t": ').strip('\n\r\t": ').strip('\n\r\t": ').replace(',','').replace('$','')
        home_details['days'] = home.find('span', {'class': 'bold'}).text.strip('\n\r\t": ').strip('\n\r\t": ').strip('\n\r\t": ')
        home_details['agent'] = home.find('div', {'class': 'capitalize bold'}).text.strip('\n\r\t": ').strip('\n\r\t": ').strip('\n\r\t": ')
        home_details['office'] = home.find('div', {'class': 'capitalize ellipse'}).text.strip('\n\r\t": ').strip('\n\r\t": ').strip('\n\r\t": ')
        home_details['neighborhood'] = homes['neighborhood']['subdivisions']
        resultset.append(home_details)                          

    return resultset

    
  # def har_homes():
#     urls = ["https://www.har.com/mapsearch/?subdivisions=NorthWest+Park+place&region_id=1&for_sale=1",
#             "https://www.har.com/mapsearch/?subdivisions=lismore+lake+estates&for_sale=1",
#            "https://www.har.com/mapsearch/?subdivisions=lakewood+oaks+estates&region_id=1&for_sale=1",
#            "https://www.har.com/mapsearch/?subdivisions=Riata+West&region_id=1&for_sale=1",
#            "https://www.har.com/mapsearch/?subdivisions=Saddle+Ridge+Estates&region_id=1&for_sale=1"]

#     all_homes = []

#     for index,url in enumerate(urls):
#         html = requests.get(url).text
#         soup = BeautifulSoup(html, "html.parser")
#         homes = soup.findAll('div', {"class": "map_prop_item pointer"})
#         neighborhood = dict(parse.parse_qsl(parse.urlsplit(url).query))
#         home_info = dict()
#         home_info['home_url'] = homes
#         home_info['neighborhood'] = neighborhood    
#         all_homes.append(home_info)

#     resultset = []

#     for homes in all_homes:
#         for home in homes['home_url']:
#             home_details = dict()
#             home_details['address'] = home.find('div', {'class': 'mpi_info'}).text.strip('\n\r\t": ').strip('\n\r\t": ').strip('\n\r\t": ').split('\n')[0]
#             home_details['price'] = home.find('div', {'class': 'price'}).text.strip('\n\r\t": ').strip('\n\r\t": ').strip('\n\r\t": ')
#             home_details['days'] = home.find('span', {'class': 'bold'}).text.strip('\n\r\t": ').strip('\n\r\t": ').strip('\n\r\t": ')
#             home_details['agent'] = home.find('div', {'class': 'capitalize bold'}).text.strip('\n\r\t": ').strip('\n\r\t": ').strip('\n\r\t": ')
#             home_details['office'] = home.find('div', {'class': 'capitalize ellipse'}).text.strip('\n\r\t": ').strip('\n\r\t": ').strip('\n\r\t": ')
#             home_details['neighborhood'] = homes['neighborhood']['subdivisions']
#             resultset.append(home_details)  