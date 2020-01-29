import urllib.request as urllib
from bs4 import BeautifulSoup
import csv
import re
def stripTextSummary(summary):
    return(summary.strip())
# empty array for results
results = []
# initialize the Indeed URL to url string
url = 'https://www.indeed.com/jobs?q=software+developer&l=Phoenix,+AZ&jt=fulltime&explvl=entry_level'
soup = BeautifulSoup(urllib.urlopen(url).read(), 'html.parser')
results = soup.find_all('div', attrs={'class': 'jobsearch-SerpJobCard'})

for i in results:
    title = i.find('div', attrs={"class":"title"})
    print('\ntitle:', title.text.strip())
    
    salary = i.find('span', attrs={"class":"salaryText"})
    #print('salary:', salary.replace("<span class='salaryText'>"),"")
    print('salary:', salary)
    
    company = i.find('span', attrs={"class":"company"})
    print('company:', company.text.strip())
    
    location = i.find('div', attrs={"class":"location accessible-contrast-color-location"})
    print('location:', location)
    
    summary = i.find('ul', attrs={"style":"list-style-type:circle;margin-top: 0px;margin-bottom: 0px;padding-left:20px;"})
    print('summary:', stripTextSummary(summary))
    
