# 07. 파이썬bool.py

flag1 = True
flag2 = False
flag3 = 1
flag4 = 0
flag5 = -1

print(type(flag1))
print(type(flag3))

if flag1:   print(1); # print('세미콜론은 문장이 끝났음을 의미한다')
if flag2:   print(2)
if flag3:   print(3)
if flag4:   print(4)
if flag5:   print(5)

# 파이썬은 논리값을 나타내기 위한 bool 자료형을 가지고 있지만
# C언어와 유사하게 숫자를 이용하여 논리값을 나타낼 수도 있다
# 이때, 0이 아닌 모든 수는 True로 간주한다