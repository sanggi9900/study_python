# 대입연산자 - 취급은 연산자이지만, 연산자처럼 쓰질 못함
num = 3 # 변수의 생성
print( num )
num = 6 # 값의 교체
print( num )
num1 = num # 변수의 생성(값의 복사만 한다)
print(num1, num)
# 응용 : 같은 값을 가진 변수 여러개 생성
# - 연산자로써, 우측부터 처리한다는 특성을 보인다.
# - 중간에 연산식이 들어가면 안됨. 생성/값의 변경만 가능
value1 = value2 = value3 = 10
print(value1, value2, value3)