# web1.py
from bs4 import BeautifulSoup

#페이지를 로딩(유니코드를 지칭): 연속적으로 메서드, 함수를 호철(메서드 체인)
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()  ##utf-8 유니코드라는 의미
#검색이 용이한 객체:정해진 상수
soup = BeautifulSoup(page, "html.parser")
# print(soup.prettify())

#<p> 몽땅 검색
# print(soup.find_all("p"))
#<p> 태그 한개 검색
# print(soup.find("p"))

#<p class="outer-text"> 약간의 검색 조건
print(soup.find_all("p", class_="outer-text"))

#태그는 삭제하고 컨텐츠만 가져오기
for tag in soup.find_all("p"):
    #앞뒤에 태그를 삭제하고 컨텐츠 : ~.text
    content = tag.text
    print(content.strip())