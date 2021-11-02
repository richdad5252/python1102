# DemoDict.py
device = {"아이폰":5, "아이패드":10, "윈도우":20}

print(type(device))
print(device)
#입력 무조건 key를 기준으로 한다.
device["맥북"] = 15
#검색
print(device["아이폰"])
#수정
device["아이폰"] = 6
#삭제
del device["아이패드"]
print(device)

#참조를 복사
device2 = device #device는 본명, device2는 별명
print(device2)
device2["LG그램"] = 40
print("--참조를 복사--")
print(device)
print(device2)
print(id(device), id(device2))

