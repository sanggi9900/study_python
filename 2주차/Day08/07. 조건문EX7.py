# 자료
num1 = int(input("첫번째 입력 >> "))
num2 = int(input("두번째 입력 >> "))

# 처리
if num2 == 0:
    result = "연산불가"
elif num1 % num2 == 0:
    result = num1 // num2
else:
    result = "%.1f"%(num1 / num2)

# 정보
print("결과 : ", result)
    