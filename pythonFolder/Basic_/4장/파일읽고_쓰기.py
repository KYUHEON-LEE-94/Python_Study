#파일 생성
from asyncore import write


f = open('text.txt', 'w');
for i in range(1,10):
    data = "%d번째 줄입니다. \n" %i
    f.write(data);

f = open('text.txt', 'r');
while True:
    line = f.readline();
    if not line: break #기억해놔라 이 문법
    print(line)
f.close

#readlines함수 사용

f = open('text.txt', 'r');
lines = f.readlines();
for line in lines:
    line = line.strip(); 
    print("readlines"+line)
f.close
    # readline, readlines함수는 /n가 자동으로 추가되어있음
    #줄 바꿈을 지울려면 strip() 사용

f = open('text.txt', 'r');
lines = f.read();
print("read()"+ lines )
f.close
#read()는 파일의 전체 내용을 읽어옴 -> 맨앞에 read()를 붙이고 나머지 전체를 읽어오게 되는 원리

#파일에 새로운 내용 추가
f = open('text.txt', 'a');
for i in range(11,20):
    data = "%d번째 줄입니다. \n" %i
    f.write(data);
f.close;

#with문과함께 사용하기
with open("ttext.txt", 'w') as f:
    f.write('python is interesting');
#with 블럭을 벗어나는 순간 close()실행
