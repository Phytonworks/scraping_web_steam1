import requests
from bs4 import BeautifulSoup

url = 'https://store.steampowered.com/'
headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
steam = soup.findAll('div', attrs={'class':'carousel_items'})

for steams in steam:
    print(steams)