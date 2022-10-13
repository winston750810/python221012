#Java, C#은 클래스나 구조체만 만들 수 있다.
#파이썬은 함수도 만들고 클래스도 만들 수 있다.

# 정적메서드.py
class MyCalc(object):
    @staticmethod
    def my_add(x,y):
        return x+y

#클래스에서 직접 호출한다.
a = MyCalc.my_add(5,7)
print(a)

