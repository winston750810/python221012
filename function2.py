# function2.py
#교집합 문자를 리스트로 리턴
from re import X


def intersect(prelist, postlist):
    #지역변수 리스트로 초기와
    result = []
    #H(0)|A(1)|M(2)
    for x in prelist:
        # 특정 글자가 postlist에 있고 result에 없으면 추가
        if x in postlist and x not in result:
            result.append(x)
    return result

#호출
print(intersect("HAM", "SPAM"))



print("-------지역변수 , 전역변수-------")
#전역변수
x = 5
def func1(a):
    return a + x

#호출
print(func1(1))

def func2(a):
    #지역변수
    x = 2
    return a + x
    
#호출
print(func2(1))

#참조를 전달하는 방식(입력 + 출력)
wordlist = ["J", "A" , "M"]
def change(x):
    x[0] = "H"

#호출
change(wordlist)
print("함수 호출후 : {0}".format(wordlist))


print("-------복사본 사용-------")
#복사본 사용(원본을 수정하기 싫을 때)
wordlist = ["J", "A" , "M"]
def change(x):
    #Deep copy(진짜 복사본 사용) : 지역변수
    x1=x[:]
    x1[0]="H"
    print("함수 내부 : {0}".format(x1))

#호출
change(wordlist)
#원본을 복사해서 사용했기 때문에 원본은 그대로 JAM 출력
print("함수 호출후 : {0}".format(wordlist))