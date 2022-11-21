# HTML 응답코드 확인(naver)
import requests

response = requests.get('https://www.naver.com')
# 응답상태 확인
print(response.status_code)
