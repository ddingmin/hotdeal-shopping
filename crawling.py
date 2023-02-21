import requests
from bs4 import BeautifulSoup



url = 'https://www.fmkorea.com/hotdeal'
domain = 'https://www.fmkorea.com'
response = requests.get(url)

def get_hotdeal_items():
    titles = []
    links = []
    numbers = []
    infos = []
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        datas = soup.select('#bd_1196365581_0 > div > div.fm_best_widget._bd_pc > ul > li > div > h3 > a')
        others = soup.select('#bd_1196365581_0 > div > div.fm_best_widget._bd_pc > ul > li > div > div.hotdeal_info')
        for data in datas:
            titles.append(data.get_text(strip = True))
            links.append(domain + data['href'])
            numbers.append(int(data['href'][1:]))
        
        for other in others:
            infos.append(other.get_text(strip = True))
    else:
        # 크롤링 실패시 에러 메시지
        print(response.status_code)
    return titles, links, numbers, infos
