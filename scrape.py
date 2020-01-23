import urllib.request as urllib
from bs4 import BeautifulSoup
import time
#establish what page we use
url = 'https://socialblade.com/youtube/top/50/mostviewed'
#load the page. make a web request
request = urllib.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
page = urllib.urlopen(request)
soup = BeautifulSoup(page, 'html.parser')

soup.find('div', attrs={'style': 'float: right; width: 900px;'}).find_all('div', recursive=False)
