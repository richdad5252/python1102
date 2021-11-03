# class1.py
#1)클래스 형식을 정의
class Person:
    #초기화메서드(생산자)
    def __init__(self):
        self.name = "default name"
    #인스턴트 메서드
    def print(self):
        print("이름은 ", self.name)

#2) 인스턴스 생성
p1 = Person() 
p2 = Person()
p1.print()
p2.print()