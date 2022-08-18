g = {"a": [1, 2, 3], "b": {0: 1, 1: 2}}
print(g["b"][0])

d = [1,2,30]
d[0] = d[0]*10;
print(d)

e = list(range(4))
e.append(5);
print(e);
del e[1]; #지우는 명령어
print(e);

#슬라이싱
ap = list(range(20))
print(ap[0:5]);
print(ap[:5]); #0은 생략가능

#복수 할당
h = [1,2,3]
h1,h2,h3 = h;
print(h1,h2,h3) #단 복수 할당을 할 때는 값이 들어갈 변수의 개수와 리스트의 길이가 같아야 한다. 그렇지 않으면 오류가 발생한다.