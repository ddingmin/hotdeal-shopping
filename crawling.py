import requests
from bs4 import BeautifulSoup

url = 'https://www.fmkorea.com/hotdeal'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select('#bd_1196365581_0 > div > div.fm_best_widget._bd_pc > ul > li > div > h3 > a')
    for item in items:
        print(item.get_text().strip())
else : 
    print(response.status_code)