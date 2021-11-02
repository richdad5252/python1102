#DemoDic2.py

tel = {"kim":"1111", "lee":"2222"}

phone = tel

print(tel)
print(phone)
print(tel)

#불린(bool)
isRight = True
print(type(isRight))
x = 5
y = 5

print(x == y)
print(x != y)
print(2>1)
print(5/2) #정수를 정수로 나누지만 실수로 결과 값이 표현됨.
print(5//2) #정수 값이 필요할 때는 슬래쉬 2개로 한다.
print(5%2) # 나머지 값을 구하는 연산자

#and는 ~이고, ~이면서
#or연사자는 ~이거나
print(True and True and True)
print(True and True and False)
print(True or False or False)

#파이썬의 판단 근거
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("demo"))
print(bool([1,2,3]))
print(bool([]))

#얕은 복사
a = [1,2,3]
b = a
a[0] = 38
print(a)
print(b)
print(id(a), id(b))

print("---깊은복사---")
a=[1,2,3]
#리시트 객체의 전체를 복사해 달라
b = a
a[0] = 38
print(a)
print(b)
print(id(a), id(b))

