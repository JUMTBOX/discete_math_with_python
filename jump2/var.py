"""
변수...
"""

# 리스트 복사하기 (내장메서드 대부분이 원본 객체를 반환하기 때문인듯...)
a = [1,2,3]
print(a)
b = a[:]
print(b)

from copy import copy

a = [4,5,6]
print(a)
b = copy(a)
print(b)
c = a
print(c)

# 메모리 주소 보기
print(id(a))
print(id(b))
print(id(c))

# 같은 주소 공간의 객체인지 확인
print(a is b)
print(a is c)

# 변수 할당의 다양한 방법 (튜플, 리스트)
a,b = ('python', 'life')
print(f"a={a} \nb={b}")

(c,d) = "python", "life"
print(f"c={c} \nd={d}")

[a,b] = ["java", "javascript"]
print(f"a={a} \nb={b}")

c = d = "python"
print(f"c={c} \nd={d}")

# 두 변수의 값 바꾸기
[a,b] = [3,5] 
a,b = b,a

print(f"a={a} \nb={b}")