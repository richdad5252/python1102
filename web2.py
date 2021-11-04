# web2.py
#웹서버에 요청
import urllib.request
#웹크롤링
from bs4 import BeautifulSoup

#파일에 저장
f = open("c:\\work\webtoon.txt", "wt", encoding="utf-8")
for i in range(1,6):
    url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i) #문자열로 안 바꿔주면 에러남
    print(url)
    data = urllib.request.urlopen(url)

    #검색에 용이한 객체를 생성
    soup = BeautifulSoup(data, "html.parser")

    cartoons = soup.find_all("td", class_="title")

    #반복해서 가져오기
    for tag in cartoons:
        title = tag.find("a").text
        print(title.strip())
        f.write(title.strip() + "\n")

f.close()



