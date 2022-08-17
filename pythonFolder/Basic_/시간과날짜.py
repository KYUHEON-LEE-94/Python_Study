#datetime 패키지
import datetime as dt

x = dt.datetime.now();
print(x);
print(x.year)
print(x.weekday())

print(x.strftime("%Y년 %m월 %d일 %A"))

#날짜/시간 연산
dt1 = dt.datetime(2016,2,19,14);
dt2 = dt.datetime(2016,1,2,13);
#datetime클래스를 계산하면 timedelta  클래스 객체로 반환
td = dt1 - dt2;
print(td.days, td.seconds, td.microseconds)
print(td.total_seconds());

#반대로 datetime 클래스 객체에 timedelta 클래스 객체를 더해서 새로운 시간을 구할 수도 있다.

t0 = dt.datetime(2018, 1,1,13);
d = dt.timedelta(days=90, seconds= 2600)
print(t0 + d)

#연습문제 2.15.3
now = dt.datetime.now()
birth = dt.datetime(2023, 9,22);
remain = birth - now;
print(remain)
remain = remain.total_seconds()/60
print(round(remain))

#time 패키지는 실행을 잠시 멈추는 sleep 함수를 제공한다. sleep 함수에 n이라는 숫자를 인수로 주면 n초만큼 쉬었다가 다음 코드를 실행한다.

import time

print(1)
time.sleep(5);
print(2);