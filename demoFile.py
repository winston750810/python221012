# demoFile.py

#쿼리스트링
url = "http://www.naver.com/?page=" + str(1)
print(url)

#문자열 출력시 정렬 예시
for x in range(1,6):
    print( x, "*", x , "=", x * x )

print("---오른쪽으로 정렬 변경")
for x in range(1,6):
    print( x , "*", x , "=", str( x * x ).rjust( 3 ) )

print("이진수 {0:x}".format(10))
print("이진수 {0:b}".format(10))
print("{0:,}\n".format(1500000))

#파일 쓰기(유니코드로 저장)
f = open("c:\\work\\demo.txt" , "wt" , encoding="utf-8")
f.write("하나\n둘\n셋\n")
f.close()

#파일 읽기(유니코드로 저장)
f = open("c:\\work\\demo.txt" , "rt" , encoding="utf-8")
print(f.read())
#어디쯤 읽고 있어?
print(f.tell())
#리셋(다시 처음)
f.seek(0)
print("--readline--")
#프린터 함수내에서 \n은 안하겠다. (end="", 기본은 end="\n")
print(f.readline() , end="")
print(f.readline() , end="")

#리셋(다시 처음)
f.seek(0)
result = f.readlines()
print(result)

f.close()
