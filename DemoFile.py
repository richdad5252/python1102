# DemoFile.py

# 파일에 쓰기(write + text)
# mac, linux: /users/kim/Desktop/work 
# win : c:\\
f = open("c:\\work\\demo.txt", "wt")
f.write("첫번째\n두번째\n세번쨰\n")
# 버퍼를 비우고 작업을 종료
f.close()

# 파일을 읽기(read + text)
f = open("c:\\work\\demo.txt", "rt")
print(f.readline())
print(f.readline())
print("--하나의 문자열로 읽기---")
print(f.tell())  #어디쯤이야?
f.seek(0)        #0으로 가
result=f.read()
print(result)
print("---리스트로 받기---")
f.seek(0)
lst = f.readlines()
print(lst)
f.close()

#파일 닫았나?
if f.closed:
    print("파일을 닫았습니다.")
else:
    f.close()

#서식지정문자
print("{0:x}".format(10)) #x는 16진수
print("{0:b}".format(10)) #이진수
print("{0:,}".format(15000)) #세자리마다 쉼표 찍어주는 역할.
    