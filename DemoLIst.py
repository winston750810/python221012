# DemoLIst.py

print("-----typle-----")
tp = (1,2,3)
print(len(tp))
print(tp[0])

#함수를 정의
def calc(a,b):
    #튜플(tuple)을 활용
    return a+b, a*b

#첫열로 이동(함수 호출)
result = calc(3,4)
print(result[0])
print(result[1])

print("id:%s, name : %s" % ("kim","김유신"))

print("---set연습---")
a = {1,2,3,3}
b = {3,4,4,5}
print( a.union(b) )
print( a.intersection(b) )
print( a.difference(b) )

#타입 변경
print("--- 형식 변경---")
a = set( (1,2,3) )
print(a)
b=list(a)
print(b)
b.append(4)
print(b)

#반복구문
#디버길할 때 중단점(Break Point)
for item in b:
    print(item)