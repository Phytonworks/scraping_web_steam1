import csv

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
}
url ='https://store.steampowered.com/vr/#p=0&tab=NewReleases'

r = requests.get(url, headers)
soup = BeautifulSoup(r.text, "html.parser")

new_games = soup.findAll('a', attrs={'class':'tab_item'})
file = open('new_game.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(['Title', 'Price', 'Tags'])


for new_game in new_games:
    if(new_game.find('div', attrs={'class': 'tab_item_name'}).text != None):
        title = new_game.find('div', attrs={'class':'tab_item_name'}).text
    else:
        title=''
    if(new_game.find('div', attrs={'class':'discount_final_price'}) != None):
        price = new_game.find('div', attrs={'class':'discount_final_price'}).text
    else:
        price = ''
    if(new_game.find('div', attrs={'class': 'tab_item_top_tags'}) != None):
         tags = new_game.find('div', attrs={'class':'tab_item_top_tags'}).text
    else:
         tags=''
    file = open('new_game.csv','a',encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow([title, price, tags])
    file.close()