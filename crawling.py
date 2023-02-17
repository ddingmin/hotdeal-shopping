import requests
from bs4 import BeautifulSoup



url = 'https://www.fmkorea.com/hotdeal'
domain = 'https://www.fmkorea.com'
response = requests.get(url)

def get_hotdeal_items():
    # 제목, 주소, 사진
    items = []
    links = []
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        datas = soup.select('#bd_1196365581_0 > div > div.fm_best_widget._bd_pc > ul > li > div > h3 > a')
        for data in datas:
            items.append(data.get_text(strip = True))
            links.append(domain + data['href'])
    else: 
        print(response.status_code)
    return items, links

get_hotdeal_items()