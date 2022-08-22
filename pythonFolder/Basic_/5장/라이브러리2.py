from cgi import print_form
from socket import if_nameindex
import time

#1970년 1월 1ㅇ리 0시 0분 0초를 기준으로 지난 시간을 초 단위로 알려준다.
print(time.time())

#time.time()이 돌려준 실수값을 사용해서 연도, 월, 일, 시, 분, 초, ... 의 형태로 바꾸어 주는 함수.
print(time.localtime(time.time()))

#위 time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수이다.
print(time.asctime(time.localtime(time.time())))

#time.ctime()을 사용해 간편하게 표시할 수 있다. asctime과 다른 점은 ctime은 항상 현재 시간만을 돌려준다는 점이다.
print(time.ctime())

print(time.strftime('%a요일,%d, %B', time.localtime(time.time())))

import calendar

print(calendar.calendar(2022))
print(calendar.prmonth(2015, 8))
print(calendar.weekday(2015, 12, 2))
#-> 0~6까지 이고 무슨 요일인 지 알려줌

#monthrange(연도, 월) 함수는 입력받은 달의 1일이 무슨 요일인지와 그 달이 며칠까지 있는지를 튜플 형태로 돌려준다.

print(calendar.monthrange(2022,8))

import random

#random.randint(1,10) 1~10 사이에서 난수값을 반환

def random_pop(data):
    # number = random.randint(0, len(data)-1)
    number = random.choice(data)
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    random.shuffle(data);
    print(data);




