import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://vibe.naver.com/chart/total'
driver.get(url)
html = driver.page_source
soup = bs(html, 'html.parser')

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
