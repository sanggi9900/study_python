num = int(input("정수 입력 >> "))
# 방향이 다르면 기본적으로 합칠 수 없다. -> 방향 : 감소/증가, 곱셈/나눗셈 등

# 방법1 : 정확하게 부호를 구분하기
result = 0
value = 0
if num > 0:
    while value <= num:
        result += value
        value += 1
else:
    while value >= num:
        result += value
        value -= 1
print("합 :", result)
# 방법2 : 달라지는 것만 분리하기. 방법1을 기반으로 함.
result = 0
if num > 0:
    n1 = 0
    n2 = num
else:
    n1 = num
    n2 = 0
while n1 <= n2:
    result += n1
    n1 += 1
print("합 :", result)
# 방법3 : 골때리는 방법
result = 0
while num != 0:
    result += num
    if num < 0:
        num +=1
    else:
        num -=1
print("합 :", result)