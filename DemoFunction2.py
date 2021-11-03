# DemoFunction2.py
#기본값이 있는 경우
def times(a=10, b=20):
    return a*b

#호출
print(times())  #예상 200
print(times(5)) #예상 100
print(times(b=6)) #예상 60
print(times(a=3, b=4)) #예상 12 

#키워드 인자방식(파라메터명을 기술)
def connectURI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

#호출
print(connectURI("credu.com", "80"))
print(connectURI(port="80", server="credu.com"))

#가변인자(갯수가 정해지지 않은 경우)
def union(*ar):
    #함수 내부에 글자를 모아둘 리스트를 초기화
    result = []
    #HAM() | SPAM(1)
    for item in ar:
        #H(0) | A(1) | M(2)
        for x in item:
            #글자가 포함되어 있지 않으면 리스트를 추가
            if x not in result:
                result.append(x)
    return result

#호출
print(union("HAM", "SPAM"))
print(union("HAM", "SPAM","EGG"))

#정의되지 않은 인자: 필수와 옵션이 있는 경우
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL

#호출
print(userURIBuilder("credu.com", "80", id="kim", passwd="1234"))
print(userURIBuilder("credu.com", "80", id="kim", passwd="1234",name="mike", age="30"))

#람다함수: 이름이 없는 간결한 함수정의 문법
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))

print((lambda x:x*x)(3))
print(globals())