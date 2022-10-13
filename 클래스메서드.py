# 클래스메서드.py
# 클래스 메서드는 상속의 대상
class CoeffVar(object):
    coefficient = 1
    #데코레이터(살아있는 주석) 
    @classmethod
    def mul(cls, fact):
        return cls.coefficient * fact 

#파생형식을 정의
class MulFive(CoeffVar):
    coefficient = 5 

x = MulFive.mul(4)
print(x)


