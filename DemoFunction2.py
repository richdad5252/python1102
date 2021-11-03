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