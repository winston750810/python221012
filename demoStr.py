# demoStr.py

strA = "파이썬은 무지 강력해"
strB = "python is very powerful"

print(len(strA))
print(len(strB))

print(strB.capitalize() )
print(strB.upper() )

print(strB.count("p") )
print(strB.count("p" , 7) )
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isnumeric())

u = "<<< spam and ham >>>"
result = u.strip("<> ")
print ( u )
print ( result )
result = result.replace("spam" , "spam egg")
print( result )
lst = result.split()
print (lst)
print (":)".join(lst))