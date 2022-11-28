import pandas as pd

# 데이터 자료형
# int와 float이 섞이면 float으로 변환됨
s = pd.Series([1, 2, 3, 4.0, 5])
print(s)

for i in s:
    print(type(i))

# 여러가지 자료형이 있으면 object
s1 = pd.Series([1, '2', True, 5.0])
print(s1)

for i in s1:
    print(type(i))

# 문자열도 object
s2 = pd.Series(['a', 'b', 'c'])
print(s2)

# 직접 데이터 타입을 명시해주면 string으로 나옴
s3 = pd.Series(['a', 'b', 'c'], dtype='string')
print(s3)

# astype() 원본에 영향을 주지 않음(다시 저장해서 사용)
s.astype('string')
print(s)  # float형이 그대로 출력됨

s4 = s.astype('string')  # 새 객체에 지정해줘야 변경됨
print(s4)
