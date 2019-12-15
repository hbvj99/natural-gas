from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests

page = ('https://www.eia.gov/dnav/ng/hist/rngwhhdD.htm')

req = Request(page)

html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")
# print(soup.prettify())

date_price = []

for date in soup.find_all(True,{"class": ["B6", "B3"]}):
    date_price.append(date.text.strip())

print(date_price[:20]) # validate
