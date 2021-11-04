#연산자 오버라이드 
class NumBox(object):
	# 초기화 메서드
	def __init__(self, num):
		self.Num = num
	# +연산자를 재정의
	def __add__(self, num):
		self.Num += num
	# -연산자를 재정의
	def __sub__(self, num):
		self.Num -= num

#인스턴스 생성
n = NumBox(40)
n + 100 
print(n.Num)
n - 110 
print(n.Num)
