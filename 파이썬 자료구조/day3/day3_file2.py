# 파일 읽기
f = open('../Python Academy/파이썬 자료구조/day3/test1.txt',
         'r', encoding='utf-8')
# data = f.read()
# f.close()
# print(data)


# data2 = f.readline()
# f.close()
# print(data2)

data3 = f.readlines()
for i in data3:
    print(i, end='\n')
