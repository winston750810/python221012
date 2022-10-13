#부모 클래스
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))

#자식 클래스
class Student(Person):
    #상속 받은 메서드를 덮어쓰기(재정의 , override)
    def __init__(self, name, phoneNumber, subject, studentID):
        #명시적으로 부모 초기화 메서드 호출
        Person.__init__(self , name , phoneNumber)
        self.subject = subject
        self.studentID = studentID
     # 덮어쓰기 (재정의)
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1} , 학과 : {2} , 학번 : {3})".format(
            self.name, self.phoneNumber , self.subject, self.studentID))


p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터학과", "201122")
p.printInfo()
s.printInfo()

