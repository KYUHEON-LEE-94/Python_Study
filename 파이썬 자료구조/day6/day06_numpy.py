import numpy as np

# 데이터 타입 지정 방법
a = np.array([1, 2, 3], dtype=np.int64)
print(a.dtype)
# int64

a = np.array([1, 2, 3], dtype='int64')
print(a.dtype)
# int64

a = np.array([1, 2, 3], dtype='i8')
print(a.dtype)
# int64

# 원소가 0으로 이루어진 배열
test1 = np.zeros((2, 2))
print(test1)

# 원소가 1로 이루어진 배열
test2 = np.ones((2, 2))
print(test2)

# np.arange
test3 = np.arange(3)
print(test3)

test3 = np.arange(3, 7, 2)
print(test3)

# np.astype() : 배열의 원소가 가지는 유형을 바꾸는 함수
a = np.array([1, 2, 3])
print(a.dtype)  # 정수형으로 나옴

a2 = a.astype(np.float64)
print(a2.dtype)

# np.transpose() 행과 열을 바꾸기
a3 = np.arange(6).reshape(2, 3)
print(a3)
print(a3.transpose())

# np.append(배열1, 배열2, 축)  : 이어붙이기 함수
a4 = np.arange(6).reshape(2, 3)
a5 = np.arange(6).reshape(3, 2)
print(np.append(a4, a5))
