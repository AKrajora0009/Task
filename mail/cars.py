from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.pararius.com/apartments/amsterdam?ac=1"
# url = "https://www.sarkariresult.com/"
page = requests.get(url)
info = BeautifulSoup(page.content,'html.parser')
containers = info.findAll('section',{'class':'listing-search-item listing-search-item--list listing-search-item--featured'})
print(containers)

for link in info.findAll('a'):
  if 'href' in link.attrs:
    print(link.attrs['href'])