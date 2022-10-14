# Web1.py
#웹크롤링(수집)
from bs4 import BeautifulSoup

#페이지로딩(메서드 체인, 함수 호출 체인)
page = open("c:\\work\\test01.html" , "rt" , encoding = "utf-8").read()
#검색이 용이한 객체
soup = BeautifulSoup(page , "html.parser")
#print( soup.prettify() )

#<p> 전부 검색(List 비슷한 객체)
#print( soup.find_all( "p" ) )

#첫번째 <p>
#print( soup.find( "p" ) )

#조건이 있는 경우 : <p class = "outer-text">
#파이썬 class키워드 충돌 => class_
#print( soup.find_all( "p" , class_="outer-text" ) )

#태그를 버리고 컨텐츠만 가져오기
for tag in soup.find_all("p"):
    #태그 내부에 문자열만 가져오기
    title = tag.text.strip()
    title = title.replace("\n","")
    print(title)