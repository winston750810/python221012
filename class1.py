# class1.py

#1) 클래스 형식 정의
class Person:
    #초기화 메서드 (가장 먼저 실행)
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))


#2) 인스턴스 생성
p1 = Person()
p2 = Person()

#무조건 멤버가 public
p1.name = "전우치"

#3) 메서드 호출
p1.print()
p2.print()

#동적인 형식(코드가 샐행중-런타임)이라 변수 추가 가능
Person.title = "new title"
print( p1.title )
print( p2.title )
print( Person.title )


#클래스에 소속된 멤버 변수 예시
print("---- 클래스에 소속된 멤버 변수 예시 ----")

