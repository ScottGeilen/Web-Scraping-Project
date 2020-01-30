import urllib.request as urllib
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import pandas as pd
import csv
import re

# empty array for results
results = []
# initialize the Indeed URL to url string
url = 'https://www.indeed.com/jobs?q=software+developer&l=Tucson,+AZ&jt=fulltime&explvl=entry_level'
soup = BeautifulSoup(urllib.urlopen(url).read(), 'html.parser')
# find all the job postings on the page
results = soup.find_all('div', attrs={'class': 'jobsearch-SerpJobCard'})
# parse through job postings looking for title, salary, company, rating, location, and summary
for i in results:        
        title = i.find('div', attrs={'class':'title'})
        salary = i.find('span', attrs={'class':'salaryText'})
        company = i.find('span', attrs={'class':'company'})
        rating = i.find('span', attrs={'class':'ratingsDisplay'})
        location = i.find('div', attrs={'class':'location accessible-contrast-color-location'})
        summary = i.find('ul', attrs={'style':'list-style-type:circle;margin-top: 0px;margin-bottom: 0px;padding-left:20px;'})
        
        print('\nTITLE:', title.text.strip())
        print('COMPANY:', company.text.strip())
        if salary is not None:
            print('SALARY:', salary.text.strip())
        if rating is not None:
            print('RATING:', rating.text.strip())
        if location is not None:
            print('LOCATION:', location.text.strip())
        if summary is not None:
            print('SUMMARY:', summary.text.strip())