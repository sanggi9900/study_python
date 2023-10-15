num = 0
while num <= 0 or num >=10:
    num = int(input("1 ~ 9 중 하나를 입력 >> "))
    if num <= 0 or num >=10:
        print("재입력하세요.")
# 누적은 천편일률적으로 일정한 형태만 나오지 않는다.
# 주의사항 : 입력반복과 처리/연산 반복은 절대로 같이 돌릴 수 없다.
# 프로그램 : 자료 -> 처리 -> 정보

# 방법1 : 입력된 값을 온존시키는 방법
result = 0
value = 1
while value <= num:
    result += value
    value += 1
print("%d까지의 합 : %d"%(num, result))

# 방법2 : 입력된 값을 갈아버리는 방법
result = 0
while num >= 1:
    result += num
    num -= 1
print("합 :",result)
print("num :",num)