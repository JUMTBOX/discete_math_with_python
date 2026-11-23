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

# a[시작번호:끝번호]에서 시작 번호를 생략하면 문자열의 처음부터 끝 번호까지 
# a[시작번호:끝번호]에서 끝번호를 생략하면 시작 번호부터 구 문자열의 끝까지
# a[시작번호:끝번호]에서 둘다 생략하면 문자열의 처음부터 끝까지

# 문자열은 Immutable이다...