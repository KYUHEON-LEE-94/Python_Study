# 리스트 배열구조
import numpy as np
li1 = [1, 2, 3, 4, 'a', 'b']
li2 = [5, 6, 'c', 'd']
print(li1, type(li1))
print(li2, type(li2))

print(li1 + li2)  # 연결
print(li1 * 3)  # 반복

# 넘파이 배열구조
# 넘파이 배열을 만들때 np.array로 사용
ar1 = np.array([1, 2, 3, 4, 'a', 'b'])
print(ar1, type(ar1))  # 숫자가 문자열로 바껴서 들어감
# 정수와 실수 -> 실수
# 정수와 문자열 -> 문자열
# 실수와 문자열 -> 문자열


# 넘파이 속성
# 1차원 배열
arr1 = np.array([1.5, 20])
print(arr1, type(arr1))
print(arr1[1])

# 2차원 배열
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# 크기 shape
print("------------shape------------")
print(arr1.shape)  # 2행 1열 (2,)
print(arr2.shape)

# 차원 ndim
print("------------ndim------------")
print(arr1.ndim)
print(arr2.ndim)


# 크기 size
print("------------size------------")
print(arr1.size)
print(arr2.size)

# 원소(요소)들의 데이터 타입
print("-----------dtype------------")
print(arr1.dtype)
print(arr2.dtype)

# 넘파이 함수
print("------------넘파이 함수 -----------------------")
# 검색
print(arr1[1])
print(arr2[1][1])

arr3 = np.array([[0, 0], [0, 0]])
# 행 추가
arr3 = np.append(arr3, [[1, 1]], axis=0)  # 배열 그대로 행 추가
print(arr3)

arr4 = np.append(arr3, [[1, 1], [2, 2], [3, 3]], axis=1)  # axis=1 열추가
print(arr4)

# 삭제
# np.delete(배열,인덱스,축)
print(np.delete(arr4, 1, axis=0))
print(np.delete(arr4, 1, axis=1))
