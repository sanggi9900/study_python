# 07. 조건문EX2.py

num = int(input('정수 입력 >>> '))
# print에서 ,로 여러 값을 출력할 때 sep에 의해 구분한다
# 직접 sep값을 지정하면 지정한 글자로 구분한다

if num > 0:
    print('양수입니다')

if num % 2 == 0:
    print('짝수입니다')

print(num, '입니다', sep='')