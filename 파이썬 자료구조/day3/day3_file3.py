# csv 파일
import csv

f = open('../Python Academy/파이썬 자료구조/day3/csv_test1.csv', 'r', encoding='utf-8')
rd = csv.reader(f)  # read()를 이용하면 리더 인스턴스를 얻을 수 있따.
for row in rd:
    for col in row:
        print(col)
    print()
f.close()
