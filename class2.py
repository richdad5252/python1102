# class2.py
#1) 클래스 형식을 정의
class Person:
    #위치를 잘 본다~~
    num_person = 0
    #초기화메서드(생산자)
    def __init__(self):
        self.name = "default name"
        Person.num_person += 1
    #인스턴트 메서드
    def print(self):
        print("이름은 ", self.name)

#2) 인스턴스 생성(p1은 인스턴스, p2는 인스턴스)
p1 = Person() 
p2 = Person()
p3 = Person()

#3) 인스턴스 갯수 확인
print("몇개:", Person.num_person)

#4) 런타임(코드가 실행중)시에 변수를 추가(동적 형식의 언어)
#디자인타임(개발하고 있는 시점)
Person.title = "new title"  #클래스에 추가
print(p2.title)
print(Person.title)

#인스턴스에 추가
p1.age = 30
print(p1.age)
# print(p2.age)