import requests
from bs4 import BeautifulSoup



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'

}
url = 'https://store.steampowered.com/vr/#p=0&tab=TopSellers'
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
top_sellers = soup.findAll('a', attrs={'class':'tab_item'})

for top_seller in top_sellers:
    print('Judul :', top_seller.find('div', attrs={'class': 'tab_item_name'}).text)
    print('Gambar :', top_seller.find('div', attrs={'class': 'tab_item_cap'}).find('img'))
    print('Tags :', top_seller.find('div', attrs={'class': 'tab_item_top_tags'}).text)