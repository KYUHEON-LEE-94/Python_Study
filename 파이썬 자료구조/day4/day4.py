import requests
from bs4 import BeautifulSoup as bs

url = "https://www.naver.com/"
response = requests.get(url)
# print(response.status_code)

# html 요소 다 읽어오기
# htmltxt = response.text
# print(htmltxt)

# query Test
param = {'query': 'movie'}
#response = requests.get(url, params=param)
htmltxt = response.text
# print(htmltxt)

# BeautifulSoup 사용
response = requests.get(url)
soup = bs(response.text, 'html.parser')
# print(soup)

# 태그이름 지정
div = soup.find('div')
# print(div)

# div = soup.find_all('div')  # 모든 div태그 다 찾음
# print(div)

# 2 내용 찾기
div = soup.find('div').text
# print(div)

# 클래스로 찾기
div = soup.find('div', class_='title_area')
# print(div)
# print(div.text)

div = soup.find('strong', class_='title')
# print(div)
# print(div.text)

# 속성값 이용 - 아래와같이 검색하면 제일 첫 ul의 class이름을 가져옴
div = soup.find('ul').get('class')
# print(div)

# 속성 조회하는 미니 퀴즈

div = soup.find('ul', class_='list_nav')
print(div.text)

# id예제
div = soup.find('div', id='NM_FAVORITE')
print(div.text)

# 멜론 크롤링해보기
# 내가 직접 접속한 것과 requests를 이용하여 접속할 때의 User-Agent가 다르기 때문에 크롤링이 안될 수 있음
# 무분별한 크롤링 방지
# 이럴때는 user-agent를 넣어주거나 바꿔줘야함
url = "https://www.melon.com/chart/index.htm"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
response = requests.get(url, headers=header)
print(response.status_code)

# Vive html 코드
url = 'https://vibe.naver.com/today'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
print(response.status_code)
