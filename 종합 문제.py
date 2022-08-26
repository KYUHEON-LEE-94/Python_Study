from functools import reduce
from operator import le
#Q1 문자열 바꾸기


# Q = 'a:b:c:d'.split(':');
# print('#'.join(Q))

# #Q2 딕셔너리 값 추출하기
# a = {'A':90, 'B':80}
# print(a.get('C', 70)) #값을 저장해주는건 아님
# print(a)

#Q3

# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# sum = 0;
# for i in A:
#     sum += i
# print(sum)

#Q5  피보나치 함수
# getNo = int(input());

# def fib(getNo):
#     if getNo == 0: return 0;
#     if getNo == 1: return 1;
#     return fib(getNo-2) + fib(getNo-1)

# for i in range(getNo):
#     print(fib(i))

#Q6
# arr = input("숫자들을 ,로 구분해서 입력:")
# arr2 = arr.split(',');
# arr3 = [];
# for i in arr2:
#     arr3.append(int(i));

# print(arr3)
# print(reduce(lambda x,y: x+y, arr3))

#Q7
# gugu = int(input());

# for i in range(1,10):
#     print('%d * %d = %d' %(gugu,i,(gugu*i)) )

#Q8

# f = open("abc.txt", 'r');

# alline = f.readlines();
# f.close;

# alline.reverse();

# f = open("abc.txt", 'w');
# for line in alline:
#     line = line.strip();
#     f.write(line);
#     f.write('\n');

# f.close();

#Q9

value = [];
f = open("sample.txt", 'r');
all = f.readlines();


def readValue():
    for line in all:
        line = line.strip();
        line = int(line);
        value.append(line)
    print(value);
f.close();
readValue();

value.index

total = reduce(lambda x,y: x+y, value)

avarage = int(total/len(value))
total = str(total)
avarage = str(avarage)


f = open("result.txt", 'w')
f.write("합계: "+total+" 평균: "+avarage)
f.close();


