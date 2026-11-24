"""
리스트는 리터럴로 만들수도 있고, 생성자로 만들수도 있다... 
"""
l = [1,2,3]
print(l)

temp = [4,5,6]
l = list(temp)
print(l)

l = list()
l.append(7)
l.append(8)
l.append(9)
print(l)

# 리스트 역시 +를 사용할 수 있고 *를 사용해서 반복할 수 있다.
a = [1,2,3]
b = [4,5,6]
print(a + b) 

print(a*3)

# 길이는 문자열과 마찬가지로 len
print(len(a))

# 리스트 요소 값 수정하기
a[2] = 4
print(a)

# 리스트 요소 삭제하기
del a[2]
print(a) # [1,2]

# 슬라이싱을 이용하여 여러 요소 삭제하기
a = [1,2,3,4,5]
del a[2:]
print(a) # [1,2]

"""
list 내장 함수

append(x)
sort() ==> 문자는 알파벳 순서
reverse()
index(x)
insert(a,b) ==> a 인덱스 위치에 b 삽입
remove(x)
pop() or pop(x) ==>  x 인덱스 위치의 요소를 반환하고 그 요소를 삭제
count(x)
extend(xlist) ==> 기존 리스트에 xlist 리스트를 더함
"""

"""
튜플...
- 1개의 요소만을 가질 때는 요소 뒤에 쉼표를 반드시 붙여야 함
- 소괄호를 생략해도 됨
- 튜플은 리스트와 달리 Immutable 임
"""
tempTuple = (1,2,3)

"""
딕셔너리 - 내장 메서드

keys() ==> 리스트가 아닌 dict_keys 객체를 반환 / Iterable 하고 list() 함수를 통해 리스트로 변환할 수 있다
values() ==> dict_values 객체 반환 / 이 역시 Iterable
items() ==> dict_items 객체 반환 / 이 역시 Iterable
clear() ==> 모든 k-v 쌍 지우기
get(key)
'key' in dictionary
pop(key) ==> key가 존재하면 해당 키의 값을 반환 후 해당 k-v 쌍 삭제
"""
