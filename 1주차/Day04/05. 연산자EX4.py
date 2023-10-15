# 연산자에는 우선순위가 있다.
# ** > * > ( /,//,%) > (+,-)
# - 연산자 우선순위에 조심해서 연산식을 작성한다.
# - 우선순위보다 먼저 처리될 내용이 있으면
# 소괄호로 묶어주면 됨.
num1 = float(input("첫번째 실수 입력 >> "))
num2 = float(input("두번째 실수 입력 >> "))
num3 = float(input("세번째 실수 입력 >> "))
# 실수형변환은 적용범위가 넓습니다.

# 팁 : 변수로 빼는 것은 먼저 다 만들고나서 판단한다.
value1 = num1 + num2 + num3
print("합 :", value1)
average = value1 / 3
print("평균 :", average)
print("정수부 :", int(average))
print("실수부 :", average % 1)