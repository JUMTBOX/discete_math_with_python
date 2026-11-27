"""
try-with 리소스 문이랑 비슷한거

with
"""

def caseBefore():
    f = open("foo.txt", "w")
    f.write("Life is too short, you need python")
    f.close()

def caseAfter():
    with open("foo.txt", "w") as file:
        file.write("Life is too short, you need python")

"""
with 블록 안에서 만든 변수를 블록 밖에서도 사용할 수 있다.
 파이썬에서 if, for, while, with 블록은 변수의 사용 범위를 제한하지 않기 때문이다.
"""

"""
sys 모듈을 사용하여 프로그램에 인수를 전달할 수 있다.
"""
import sys

# > python jump2/file.py aaa bbb ccc
# aaa
# bbb
# ccc
args = sys.argv[1:]
for i in args:
    print(i)