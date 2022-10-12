# demoIndex.py
strA="python is powerful"
strB="파이썬은 강력해"
print( strA[0] )
print( strA[0:6] )
print( strA[:6] )
print( strB[-3:])
print( strA[-8:])
print( strA[:])

print( strA[-11:-9])
print( strA[-18:-12])
#리스트 형식을 연습
colors=["red","blue","green"]
print(len(colors))
print(colors[0])
colors.append("black")
print(colors)

#자동완성
colors.append("white")
print(colors)
colors.insert(1,"pink")
colors +=["red"]
colors +="red"
print(colors.count("red"))
print(colors.index("red",1))
colors.append("red")
print(colors)
print(colors.count("red"))
#print(colors.sort())
print(colors.index("red"))
print(colors.index("red",1))
print(colors.index("red",2))