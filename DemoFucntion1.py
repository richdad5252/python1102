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
    #H(0) | A(1) | M(2)
    for x in prelist:
        #x라는 글자가 postlist에 있고 x가 아직 result에는 없고
        if x in postlist and x not in result: #if에서의 in은 포함 여부
            result.append(x)
    return result
    
#함수를 호출
print(intersect("HAM","SPAM"))

#w정수, 실수, 복소수, 문자열, 튜플, 불린
print("---불변형식---")
x = 1.2
print(id(x))
x = 2.3
print(id(x))

print("---가변형---")
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))
lst.remove(2)
print(id(lst))
print(lst)
print(lst[0:2])

print("---참조 인자 전달---")
#참조를 통해서 인자를 전달
def change(x):
    x[0] = "H"

#함수를 호출 # pass by reference 참조를 통해 전달한다.
wordlist = ["J","A","M"]
#참조가 복사되서 인자가 전달되었기 때문에 원본이 수정된다.
change(wordlist)
print(wordlist)

print("---지역변수 전달---")
def change(x):
    #함수 내부에 복사본을 만들어서 작업(Depp Copy)
    x1 = x[:]
    x1[0] = "H"
    print("함수내부:", x1)

#함수를 호출 # pass by reference 참조를 통해 전달한다.
wordlist = ["J","A","M"]
#참조가 복사되서 인자가 전달되었기 때문에 원본이 수정된다.
change(wordlist)
print(wordlist)


#전역변수와 지역변수
x = 1   #전역 변수
def func(a):
    return x+a

#함수 호출
print(func(1))

def func2(a):
    x=5
    return x+a

#함수 호출
print(func2(1))