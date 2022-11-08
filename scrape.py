import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
from bs2json import bs2json

context = ssl._create_unverified_context()

res = urlopen("https://powerball.com/",
              context=context)
soup = BeautifulSoup(res, "html.parser")
data = soup.findAll("ul", "winning-numbers")
converter = bs2json()
json = converter.convertAll(data, join=True)

for item in data:
    # print(item.get_text())
    print(json)
