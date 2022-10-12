# function1.py
#1)함수를 정의

import re


def setValue(newValue):
    #지역변수로 초기화
    x = newValue
    print("함수내부 : {0}".format(x))
#2)함수를 호출
retValue = setValue(5)
print(retValue)

#함수정의
def swap(x,y):
    return y,x

#호출
print(swap(3,4))
result = list(swap(3,4))
print(result)
