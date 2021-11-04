# -*- 생성자와 소멸자 그리고 참조 카운트 관리  -*-
class MyClass:
    #초기화(생성자)메서드
    def __init__(self, value):
        self.value = value
        print("Instance is created! Value = ", value)
    #소멸자 메서드:유명무실하다~~
    def __del__(self):
        print("Instance is deleted!")

#인스턴스 생성 
d = MyClass(10)
#사용이 끝난 경우
#del d

print("전체 코드 실행 종료")




