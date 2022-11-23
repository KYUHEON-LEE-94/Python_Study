import requests
from bs4 import BeautifulSoup as bs
import csv

# 1
# url = "https://sports.news.naver.com/kbaseball/record/index?category=kbo"
# response = requests.get(url)
# soup = bs(response.text, 'html.parser')
# div = soup.select('td.tm')

# for idx, i in enumerate(div):
#     print(f'{idx+1}위{i.text.strip()}')

# 2
f = open('csv_melon.csv', 'w', encoding='utf-8')
rd = csv.writer(f)

url = "https://www.melon.com/chart/index.htm"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
response = requests.get(url, headers=header)
soup = bs(response.text, 'html.parser')
div = soup.select('span.checkEllipsis')
for idx, i in enumerate(div):
    song = soup.select('div.ellipsis')[idx+12].text
    rd.writerow([song, i.text.strip()])
f.close()


# 3
# f = open('moive_rank.txt', 'w', encoding='utf-8')
# url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"
# response = requests.get(url)
# soup = bs(response.text, 'html.parser')
# div = soup.select('td.title')

# for idx, i in enumerate(div):
#     string = "%d 위 %s \n" % (idx+1, i.text.strip())
#     f.write(string)
# f.close()
