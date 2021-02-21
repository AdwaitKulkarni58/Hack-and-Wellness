from bs4 import BeautifulSoup
import requests
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv


URL = 'https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases'
headers ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
confirmed =[]
deaths = []
countries = []

for item in soup.select('table tr'):
    try:
        print('----------------------------------------------------------------')
        region = item.select('td')[0].get_text()
        print('Region: ' + region)


        country = item.select('td')[1].get_text()
        print('Country: ' + country)

        sum_of_cases = item.select('td')[2].get_text()
        print('Sum of cases: ' + sum_of_cases)

        deaths = item.select('td')[3].get_text()
        print('Deaths: ' + deaths)

        confirmed_cases_during_quarantine = item.select('td')[4].get_text()
        print('Confirmed cases during quarantine: ' + confirmed_cases_during_quarantine)

    except Exception as e:
        print('')


        

        



