"""
집합 자료형 Set
- 중복을 허용하지 않고
- 순서가 없다 (unordered)
"""
# 인수로 리스트 혹은 문자열을 넘기며 생성자로 만들 수 있다
set1 = set([1,2,3])
print(set1)
set2 = set("hello")
print(set2)

set3 = {1,2,4}
print(set3)


# 교집합
print(set1 & set3)
print(set1.intersection(set3))

# 합집합
print(set1 | set3)
print(set1.union(set3))

# 차집합
print(set1 - set3)
print(set1.difference(set3))


"""
add(x) ==> 요소 x 1개 추가
update([x,y,z]) ==> 요소 여러개 추가
remove(x) ==> set에 x가 존재하지 않을시 에러
discard(x) ==> set에 x가 존재하지 않아도 에러가 발생하지 않음
clear() ==> 모든 값 제거
"""

"""
Bool 자료형

JS랑 다르게 리스트,튜플, 딕셔너리가 비어있다면 Falsy 취급 된다고 함
"""

# bool 함수
print(bool('python'))   # True
print(bool(''))         # False

# and, or, not 논리 연산
print(True and True)    # True
print(True or False)    # True
print(not False)        # True

print(False and True)   # False
print(False or False)   # False
print(not True)         # False

# 나머지 Truthy / Falsy 값들도 동일하게 동작