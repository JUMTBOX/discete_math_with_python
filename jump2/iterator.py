def coffee_machine():
    coffee = 10

    while True:
        money = int(input("돈을 넣어 주세요: "))
        if money == 300:
            print("커피를 줍니다.")
            coffee -= 1
        elif money > 300:
            print(f"거스름돈 {money - 300}을 주고 커피를 줍니다")
            coffee -= 1
        else: 
            print("돈을 다시 돌려주고 커피를 주지 않습니다.")
            print(f"남은 커피의 양은 {coffee} 개 입니다.")

        if coffee == 0:
            print("커피가 다 떨여졌습니다. 판매를 중지 합니다.")
            break

"""
while-else문
while 문의 조건이 거짓이 되어 정상적으로 끝나면 else 절이 실행되고, break로 빠져나가면 esle절은 실행되지 않는다
"""
i = 0
while i < 3:
    i += 1
else: print("else문 실행임")    
 
"""=====================================================
range 객체

range(10)           ===> 0 ~ 10미만의 숫자를 포함하는 range 객체를 만들어준다
range(start, end)   ===> start ~ end미만의 숫자를 포함하는 range 객체를 만들어준다
"""
sum = 0
for i in range(1,11):
    sum += i

print(f"sum= {sum}")

# 리스트를 인덱스로 순회하는 방법?
# 
# const arr = [1,2,3,4,5];
# for(let i = 0; i < arr.length; i++) {
#   console.info(arr[i])
# }
list = [1,2,3,4,5]
for i in range(len(list)):
    print(f"list[{i}] = {list[i]}")

# list comprehension
result = [elem * 3 for elem in list]
print(result)
# [표현식 for 항목 in 반복_가능_객체 if 조건문]
result = [elem * 3 for elem in list if elem % 2 != 0]
print(result)

"""
for-else 문 
 for 문이 끝까지 수행되면 else 절이 실행되고, break로 빠져나가면 else 절은 실행되지 않는다
"""

# enumerate 함수
fruits = ["apple", "banana", "orange"]
for i,fruit in enumerate(fruits):
    print(f"index:{i} : {fruit}")


# i 시작 번호를 바꾸고 싶다면
for i,fruit in enumerate(fruits, 1):
    print(f"index:{i} : {fruit}")


# zip 함수로 여러 리스트 함께 순회 
names = ["홍길동", "김철수", "이영희"]
koreans = [85, 92, 78]
english = [90, 88, 95]

for name, kor, eng in zip(names, koreans, english):
    print(f"{name}: 국어:{kor}점, 영어:{eng}점")