import urllib.request as urllib
from selenium.webdriver import Chrome
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import csv
import re

# pageNumber = 10
url = 'https://www.indeed.com/jobs?q=software+developer&l=Tucson,+AZ&jt=fulltime&explvl=entry_level'
driver = webdriver.Chrome()
driver.get(url)
results = []
soup = BeautifulSoup(urllib.urlopen(url).read(), 'html.parser')

# find all the job postings on the page
results = soup.find_all('div', attrs={'class': 'jobsearch-SerpJobCard'})

# parse through job postings looking for title, salary, company, rating, location, and summary
file = open('jobs.csv', 'wb')
writer = csv.writer(file)

# write header row in csv file
# writer.writerow(['title', 
#                  'salary', 
#                  'company', 
#                  'rating', 
#                  'location', 
#                  'summary'])

# Search
for i in results:
        # find the html elements to scrape
        title = i.find('div', attrs={'class':'title'})
        salary = i.find('span', attrs={'class':'salaryText'})
        company = i.find('span', attrs={'class':'company'})
        rating = i.find('span', attrs={'class':'ratingsDisplay'})
        location = i.find('div', attrs={'class':'location accessible-contrast-color-location'})
        summary = i.find('ul', attrs={'style':'list-style-type:circle;margin-top: 0px;margin-bottom: 0px;padding-left:20px;'})

        # strip the html tags and stuff from the text i actually need
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
        
        
        # writer.writerow([
        #     title.encode('utf-8'), 
        #     salary.encode('utf-8'), 
        #     company.encode('utf-8'), 
        #     rating.encode('utf-8'), 
        #     location.encode('utf-8'),
        #     summary.encode('utf-8')])
        
        # Go to next pages
        # pageNumber = pageNumber + 10
        # nextPage = 'https://www.indeed.com/jobs?q=software+developer&l=Tucson%2C+AZ&jt=fulltime&explvl=entry_level&start=' + str(pageNumber)
        # while pageNumber <= 40:
        #     driver.get(nextPage)
driver.close()
