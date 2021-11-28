from bs4 import BeautifulSoup
import requests
# from csv import writer
#
# # url = "https://www.pararius.com/apartments/amsterdam?ac=1"
url = "https://www.sarkariresult.com/"
#
page = requests.get(url)
#
soup = BeautifulSoup(page.content,'html.parser')
lists = soup.find('box1','docs-creator')
print(lists)


 # listing-search-item--list listing-search-item--featured
# with open('housing.csv','w',encoding='utf8',newline='') as f:
#     thewriter=writer(f)
#     header =['Title','Location','Price','Area']
#     thewriter.writerow(header)

# for list in lists:
#     title = list.find('a', class_="listing-search-item__link listing-search-item__link--title docs-creator").text.replace('\n','')
#     location = list.find('div',class_="listing-search-item__location").text.replace('\n','')
#     price = list.find('div',class_='listing-search-item__price').text.replace('\n','')
#     area = list.find('span',class_='illustrated-features__item illustrated-features__item--surface-area').text.replace('\n','')
#
#         # info =[title, location, price, area]
#         # thewriter.writerow(info)
#     print(list)

#
# from bs4 import BeautifulSoup
# import requests
# from csv import writer
#
# url = "https://www.pararius.com/apartments/amsterdam?ac=1"
# # url = "https://www.sarkariresult.com/"
# page = requests.get(url)
# soup = BeautifulSoup(page.content,'html.parser')
# containers = info.findAll('section',{'class':'listing-search-item listing-search-item--list listing-search-item--featured'})
# print(containers)
#
# for link in info.findAll('a'):
#   if 'href' in link.attrs:
#     print(link.attrs['href'])