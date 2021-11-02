# DemoFucntion1.py
#함수를 저으이
def setValue(newValue):
    x = newValue   #지역변수 x에다가 넘겨.

#함수를 호출
result = setValue(5)
print(result)

#함수를 저으이
def swap(x,y):
    return y,x

#호출
print(swap(5,6))

#디버깅 연습을 위한 함수(교집합 문자를 만들기)
def intersect(prelist, postlist):
    #지역변수에 리스트로 저장하기
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result
    
#함수를 호출
print(intersect("HAM","SPAM"))