# 07. 조건문else.py

num = int(input('정수 입력 >>> '))

if num % 2 == 0:
    print('짝수')

# else는 이전에 등장한 if의 조건이 거짓인 경우이므로
# 별도의 조건을 가지지 않는다

# if not num % 2 == 0:
else:   
    print('홀수')

