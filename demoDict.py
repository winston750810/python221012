# demoDict.py

device = {"아이폰":5 , "아이패드":10 , "윈도우":20}
print(len(device))
print(device["아이폰"])
device["맥북"]=15
print(device)
del device["아이패드"]
print(device)

for item in device.items():
    print(item)

for k,v in device.items():
    print( k , v )

phone = {"kim":"1111" , "lee":"2222"}
print(phone.keys())
print(phone.values())
print("kim" in phone)
print("moon"in phone)
print("moon" not in phone)

#참조를 복사 (Pass By Reference)
p=phone
p["kang"]="1234"
print(phone)
print(p)
print(id(phone), id(p))

print("------논리식 출력-----")
print( 1 < 2 )
print( 1 != 2 )
print( 1 == 2 )
print(True and True and True)
print(True and True and False)
print(True or False or False)

print("-----bool()-----")
print(bool(0))
print(bool(3))
print(bool(""))
print(bool("demo"))
print(bool([]))
print(bool([1,2,3]))
