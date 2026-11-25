"""
변수 scope 알아보기
"""

if True:
    a = 10

print(a)

"""
키워드

global     ---> 모듈 전역 변수에 대한 바인딩
nonlocal   ---> 외부 함수 변수에 대한 바인딩
키워드X    ---> 함수 내부에서 이름에 할당하면 지역 변수로 취급 
"""

x = 10

def temp():
    global x
    print(f"재할당 이전 {x}")
    x = 20
    print(f"재할당 이후1 {x}")

temp()

print(f"재할당 이후2 {x}")


y = 10

def tmp():
    # print(f"재할당 이전 {y}") --->  바깥 y를 참조하지 않고 UnboundLocalError 오류 발생  "cannot access local variable 'y' where it is not associated with a value"
    y = 20
    print(f"재할당 이후1 {y}")

tmp()

print(f"재할당 이후2 {y}")