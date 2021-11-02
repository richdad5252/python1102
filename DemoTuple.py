# DemoTuple.py
tp = (1,2,3)
print(type(tp))
print(len(tp))
print(tp[1])

#함수를 정의
def calc(a,b):
    return a+b, a*b
    
#함수를 호출
result = calc(3,4)
print(result)

print("id: %s, name: %s" % ("kim", "김유신"))

#한번에 묶어서 입력 데이터 전달
args = (5,6)
print(calc(*args))

#형식을 변환
a = set((1,2,3))
print(a)
print(type(a))
b=list(a)
print(b)
b.append(4)
print(type(b))

#사전식
color = {"apple":"red", "kiwi":"green"}
print(type(color))
print(len(color))
print(color["apple"])
#입력
color["cherry"] = "red"
#items()메서드는 키와 값을 동시에 반환
#디버깅 모드인 경우 무조건 중지(Break Point)
for item in color.items():
    print(item)

for k,v in color.items():
    print(k, v)

#키만 출력
for k in color.keys():
    print(k)

#값만 출력 #키의 메서드
for v in color.values():
    print(v)