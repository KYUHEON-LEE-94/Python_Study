import requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # 내부 창을 띄울 수 없으므로 설정
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# wd라는 객체에 크롬 드라이버를 넣음
wd = webdriver.Chrome('chromedriver', chrome_options=chrome_options)

# 드라이버가 찾아서 들어온 것으로 생각, 설치해줘야하는 경우가 있으면 드라이버 설치해주면됨

wd.get("https://vibe.naver.com/chart/total")
# 이 url에 접근하겠다.
html = wd.page_source
soup = bs(html, 'html.parser')
# print(soup)

# 순위 가수명 등을 리스트로
song_box = soup.find("tbody")
songs = song_box.select("td.song")

song_rank = []
rank = 1
for i in songs:
    ranks = str(rank)+"위"
    title = i.select_one('a.link_text').text
    singers = i.select_one('a.link_artist').text
    song_rank.append([ranks, title, singers])
    rank += 1
print(song_rank)
