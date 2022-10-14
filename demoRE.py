# demoRE.py
#정규표현식(특정한 패턴을 검색)

import re
#포함하고 있는 경우
result = re.search("[0-9]*th" , " 35th")
print (result)
print(result.group())

# #정확하게 일치하는 경우만
# result = re.match("[0-9]*th" , "  35th")
# print (result)
# print(result.group())

print("---우편번호---")
result = re.search("\d{5}" , "우리 동네는 12457")
print(result.group())

print("---연도---")
result = re.search("\d{4}" , "올해는 2022년입니다.")
print(result.group())

result = re.search("apple".lower() , "this is Apple".lower())
print(result.group())