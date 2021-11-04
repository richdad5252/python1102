# DemoRE.py
#정규표현식
import re #regular expression의 앞글자를 짠것.

#찾았으면 매칭 객체 리턴
result = re.search("[0-9]*th", "35th")
print(result)
print(result.group())

#match함수, search함수 비교
#match는 정확하게 일치
#search는 포함하고 있다면
print(bool(re.match("ap", "this is apple")))
print(bool(re.search("ap", "this is apple")))

print("---년도---")
print(bool(re.match("\d{4}", "작년은 2020년"))) #매치는 처음을 본다. 작년은을 보고 포기
print(bool(re.search("\d{4}", "작년은 2020년"))) # 서치는 계속 검색
print(bool(re.search("\d{5}", "우리동네 우편번호는 52300"))) #\d{5}는 연속으로 다섯자리 오는 숫자를 찾으라는 의미

