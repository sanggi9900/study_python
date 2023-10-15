# 출력 - 내부에 있던 것을 외부로 전달하는 과정
# ex1) 저장된 것을 화면에 보여준다.
# ex2) 이메일을 열어서 그 내용물을 본다.
# ex3) USB메모리로 컴퓨터에 있던 것을 외부로 복사한다.

# print() : print를 거치면 "뭐든" 문자로 출력이 된다.
# 상수 출력하기 : 상수들은 필요한 곳에 바로 작성하면 사용이 가능
print(123, 3.14, "Apple", True)

num = 123
fnum = 3.14
word = "Apple" # 변수에는 기본적으로 하나의 값만 저장한다.
value = False  # 변수를 만들 때는 한줄당 하나씩 만든다.

# 변수 출력하기 : 변수들이 출력하기 전에 만들어져 있어야 가능
print(num, fnum, word, value)
print(num, fnum, word, value) # 쉼표 : 문법요소 / 변수 및 상수를 구분하는 문법
print(num, num, fnum, fnum)   # 소괄호 내부에서 띄어쓰기, 엔터 등은 무시된다.