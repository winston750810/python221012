# class2.py

#클래스에 소속된 멤버 변수 예시
print("---- 클래스에 소속된 멤버 변수 예시 ----")

#1) 클래스 형식 정의
class Person:
    #클래스 멤버 변수
    num_person = 0
    #초기화 메서드 (가장 먼저 실행)
    def __init__(self):
        self.name = "default name"
        Person.num_person += 1
    def print(self):
        print("My name is {0}".format(self.name))


#2) 인스턴스 생성
p1 = Person()
p2 = Person()
p3 = Person()

print("인스턴스 개수 : {0}".format(Person.num_person))