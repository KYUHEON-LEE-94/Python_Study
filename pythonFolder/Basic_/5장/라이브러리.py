import sys
import pickle
import os
import shutil
import glob

#파일을 임시로 만들어서 사용
import tempfile

print(1)
# print(sys.exit())
print(sys.path)
#파이썬 모듈이 설치되어 있는 위치

#pickle
#객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다.

f = open('test.txt', 'wb')
data = {1: 'python', 2:'you need'}
pickle.dump(data,f)
f.close();

f = open('test.txt', 'rb')
data = pickle.load(f)
print(data)

#os 환경 변수나 디렉터리, 파일 등의 OS자원을 제어할 수 있게 해주는 모듈

print("-"*20)
print(os.environ['path'])

#os.chdir을 사용하면 현재 디렉터리 위치 변경 가능
# os.chdir("C:\WINDOWS")

print("-"*20+"os")
print(os.getcwd())

print("-"*20+"os2")

f = os.popen("dir")
print(f.read())

#shutil 파일을 복사해주는 파이썬 모듈

shutil.copy("test.txt", "test2.txt")

print("-"*20+"glob")
print(glob.glob('D:\웹개발_이규헌\Front\FrontEnd'))

#tempfile

#무작위의 파일이름 생성
filename = tempfile.mkstemp()
print(filename)

f = tempfile.TemporaryFile();
f.close()

