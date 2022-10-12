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