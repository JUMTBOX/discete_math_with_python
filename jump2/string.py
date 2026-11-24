"""
몰랐던 것 위주로
"""
# 문자열 곱하기
print("=" * 50)
print("My Program")
print("=" * 50)

# 문자열 길이 구하기
a = "Life is too short"
len(a) 
# >>> 17

# 문자열 슬라이싱
a = "Life is too short, You need Python"
a[0:4] 
# >>> Life

print(a[19:-7])
# >>> 'You need'
print(a[-2:])
# >>> 'on'

# a[시작번호:끝번호]에서 시작 번호를 생략하면 문자열의 처음부터 끝 번호까지 
# a[시작번호:끝번호]에서 끝번호를 생략하면 시작 번호부터 구 문자열의 끝까지
# a[시작번호:끝번호]에서 둘다 생략하면 문자열의 처음부터 끝까지

# 문자열은 Immutable이다...

# 문자열 포매팅
s = "I eat %d apples" % 3
print(s)

s = "I eat %s apples" % "five"
print(s)

s = "I eat %d apples. so I was sick for %s days" % (3 , "five")
print(s)

s = "Error is %d%%" % 98
print(s)

# 정렬과 공백
s = "%10s" % "hi"
print(s) # 길이가 10인 문자열 공간 맨 오른쪽에 'h', 'i'를 배치

s = "%-10sjane." % "hi" 
print(s) # 길이가 10인 문자열 공간 맨 왼쪽부터 'h', 'i'를 배치

s="{0:<10}".format("hi")
print(s) # 길이 10, 왼쪽 정렬
s="{0:>10}".format("hi")
print(s) # 길이 10, 오른쪽 정렬
s="{0:^10}".format("hi")
print(s) # 길이 10, 가운데 정렬


# 공백 채우기
s = "{0:=^14}".format(" hi ")
print(s)
s = "{0:!<10}".format("hi")
print(s)
"""
정렬할 때 공백 문자 대신 지정한 문자 값으로 채워 넣을 수도 있다. 
채워 넣을 문자 값은 정렬 문자 <, >, ^ 바로 앞에 넣어야 한다. 

위 예제에서 첫 번째는 가운데(^)로 정렬하고 빈 공간을 =로 채웠고,
두 번째 예제는 왼쪽(<)으로 정렬하고 빈 공간을 !로 채웠다.
"""

# f 문자열 포매팅 (3.6.0 버전 이상부터 사용가능...)
name = "홍길동"
age = 30 

s = f"나의 이름은 {name}입니다. 나이는 {age}입니다."
print(s)

# 딕셔너리는 f 문자열 포매팅에서 다음과 같이 사용할 수 있다.
dictionary = {"name":"홍길동", "age": "30"}
s = f"나의 이름은 {dictionary['name']}입니다. 나이는 {dictionary['age']}입니다."
print(s)

# f 문자열 포매팅에서의 정렬
s = "hi"
print(f"{s:<10}")
print(f"{s:>10}")
print(f"{s:^10}")

# 금액에 콤마 삽입하기
s = f"난 {1500000:,}원이 필요해"
print(s)

a = "Python is the best choice"
print(a.find("b"))
print(a.index("b"))

"""
count()
find()
index()
join()
upper()
lower()
lstrip()
rstrip()
strip()
replace()
split()
isalpha()
isdigit()
startswith()
endswith()
"""