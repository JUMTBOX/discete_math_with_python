"""
함수
"""

# 매개변수를 지정하여 호출하기
def add(a, b):
    print(f"a={a}, b={b}")
    return a + b 

print(add(b=3, a=10))

# 입력값이 몇 개가 될지 모를 때 (가변 매개변수)
def temp(*args):
    print(args)
    for s in args:
        print(s)

temp(1,2,3,4,5)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for num in args: result += num
    else: 
        result = 1
        for num in args: result *= num
    return result

print(add_mul("add", 1,2,3,4))
print(add_mul("mul", 1,2,3,4))

# 키워드 매개변수 ===> 입력받은 키워드 매개변수들을 딕셔너리 형태로 출력한다
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name="foo", age=3)
print_kwargs(name="홍길동", age=25, city="서울", job="개발자")


# 매개변수 초깃값 설정하기 (js와 동일)


# 응용
def add_and_mul(a,b):
    return a+b, a*b

(addResult, mulResult) = add_and_mul(3,4)

print(f"add={addResult}, mul={mulResult}")

"""
lambda 예약어
함수를 생성할 때 사용하는 예약어로, def와 동일한 역할을 한다.
"""
addLambda = lambda a,b : a + b
print(addLambda(1,1))