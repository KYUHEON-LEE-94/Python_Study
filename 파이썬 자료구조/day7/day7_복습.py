import pandas as pd

# 딕셔너리 -> 데이터프레임
student = {'math': [90, 10], 'english': [90, 10],
           'korean': [100, 10], 'his': [80, 10], 'art': [95, 10]}
df = pd.DataFrame(student)
print(df)

# 키와 컬럼명이 달라서 키를 못찾기 때문에 값을 못가져옴
df = pd.DataFrame(student, columns=['a', 'b', 'c', 'd', 'e'])
print(df)
# Empty DataFrame
#Columns: [a, b, c, d, e]

df = pd.DataFrame(student, columns=['math', 'english', 'korean', 'his', 'art'])
print(df)

# 데이터 프레임 -> 딕셔너리
# 열이름 =키 / 레코드 =값/ 인덱스=키

dict1 = df.to_dict()  # 데이터프레임df를 딕셔너리로 변환
print(dict1)

# df.to_dict('list') #열이름 =키, 값 쌍은 각각 목록으로
dict1 = df.to_dict('list')
print(dict1)

# df.to_dict('index') 인덱스 =키, 각 행 =값
dict1 = df.to_dict('index')
print(dict1)


# df.to_dict('records') 각 행을 사전형
dict1 = df.to_dict('records')
print(dict1)

# index
print(df.index)  # RangeIndex(start=0, stop=2, step=1)

# values
print(df.values)  # [[ 90  90 100  80  95]
# [ 10  10  10  10  10]]

# columns
print(df.columns)

# dtypes
print(df.dtypes)

# info(): .info()이용하여 데이터 df의 정보를 모두 출력
df.info()

# head(): .head() 상위 5행을 출력
df.head()

# tail() 하위행
df.tail()


# 3 데이터프레임 수정, 추가, 삭제
# -----------------컬럼명 수정------------

# 전체 컬럼명 수정
df.columns = ['col1', 'col2', 'col3', 'col4', 'col5']
print(df)

# 일부 컬럼명 수정
# df.rename(columns={'Before':'After'})
df.rename(columns={'col1': 'math'}, inplace=True)  # inplace를 해야 원본에도 적용됨
print(df)

# 인덱스명 수정
df.index = ['idx1', 'idx2']
print(df)

# .rename() 함수 > 일부 인덱스명 수정
df.rename(index={'idx1': 'idx50'}, inplace=True)
print(df)

# ------------------------추가---------
li1 = [[0, 0], [0, 0]]
df = pd.DataFrame(li1)
print(df)

df.columns = ['a', 'b']
print(df)

# 새로운 행을 만들기
df.loc[2] = 1
print(df)

# 새로운 열 만들기
# df['D'] = 'A'
# print(df)
# 다른 값의 다른 열 넣기
df['D'] = ['A', 'B', 'C']
print(df)

# ----값 삭제----
# 행삭제
df.drop(2, inplace=True)
print(df)

# 열삭제
df.drop('D', axis=1, inplace=True)
print(df)

# 4) 행선택(loc, iloc)

# 열 전체 값 수정
df['a'] = 1
print(df)

# 행 전체 값 수정
df.loc[2] = 'x'
print(df)

# 특정값 수정 df, loc[행인덱스, 열이름] = 새로운 값
df.loc[2, 'D'] = 'p'
print(df)

# 행 인덱스 0, 컬럼 b-> 'A'
df.loc[0, 'b'] = 'A'
print(df)

print('----')
print(df.loc[0, 'b'])
