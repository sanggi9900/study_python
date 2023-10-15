# 추가문제
# 1보다 큰 수의 약수를 구하는 문제입니다.
# 약수를 구하여 아래의 결과를 출력합니다.
# 1) 약수들의 합, 2) 약수의 수량, 3) 소수인지 여부

# 자료 : 2 이상의 값만 필요하니 1이하는 전부 재입력처리로 걸러낸다.
value = 0
while value <= 1:
    value = int(input("정수 하나 입력 >> "))

# 처리 : 준비된 자료로 원하는 것을 달성하도록 구성
result1 = 0 # 합을 누적할 변수
result2 = 0 # 수량을 누적할 변수
num = 1
while num <= value:
    if value % num == 0:
        result1 += num
        result2 += 1
    num += 1
if result2 == 2:
    result3 = "참"
else:
    result3 = "거짓"

# 정보 : 처리에서 준비된 값을 모두 출력
print("합 : %d, 수량 : %d개, 소수여부 : %s"%(result1, result2, result3))
print("약수목록")
num = 1
while num <= value:
    if value % num == 0:
        print(num, end=" ")
    num += 1
print()