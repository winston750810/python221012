# Web2.py

#웹서버에 페이지 실행 요청
import urllib.request

#크롤링
from bs4 import BeautifulSoup
for i in range(1,6):

url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page="

data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")

soup = BeautifulSoup(data, "html.parser")

#검색하기
cartoons = soup.find_all("td" , class_="title")


title = cartoons[0].find("a").text
link = cartoons[0].find("a")["href"]
print(title)
print(link)

for item in cartoons:
    title = item.find("a").text
    print(title.strip())