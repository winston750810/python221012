# try1.py
#함수 정의
def divide(a,b):
    return a/b
#에러치리
try:
    #함수호출
    result = divide(5,2) 
except ZeroDivisionError:
    print("0으로 나누면 안됩니다.")
except TypeError:
    print("형식이 숫자이어야 합니다.")
else:
    print("결과 : {0}".format(result))
finally:
    print("무조건 실행")

print("전체 코드 종료")