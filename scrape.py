import urllib.request as urllib
from bs4 import BeautifulSoup
import csv
#establish what page we use
url = 'https://socialblade.com/youtube/top/50/mostviewed'
#load the page. make a web request
request = urllib.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'})[4:]
page = urllib.urlopen(request)
soup = BeautifulSoup(page, 'html.parser')

rows = soup.find('div', attrs={'style': 'float: right; width: 900px;'}).find_all('div', recursive=False)

file = open('topyoutubers.csv', 'wb')
write = csv.writer(file)

# write header rows
writer.writerow(['Username', 'Uploads', 'Views'])

for row in rows:
    username = row.find('a').text.strip()
    numbers = row.find_all('span', attrs={'style': 'color:#555;'})
    uploads = numbers[0].text.strip()
    views = numbers[2].text.strip()

    print(username + ' ' + uploads + ' ' + views)
    writer.writerow([username.encode('utf-8'), uploads.encode('utf-8'), views.encode('utf-8')])

file.close()
# jobs = pd.DataFrame()
# jobs.to_csv('code\ScrapingIndeed\Web-Scraping-Project/jobs.csv', index=False, header=False)
# reader = csv.reader('jobs.csv')
# with open('jobs.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Hello, world"])