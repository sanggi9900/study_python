# 자료는 무조건 "하나"로 사용되는 것이 아니라 "하", "나"로 사용될 수 있다.
# -> 변수에는 "하나"를 저장할 수 있고, "하","나"는 안된다.

# 리스트 : 자료"들"을 보관하기 위한 자료구조
# 1. 미리 넣어두기 : 미리 준비하면 쓸만하니까, 좋으니까....
# - 명칭은 복수형 또는 lst를 쓴다.
# - list는 쓰면 안됨
values1 = [ 0, 0, 0 ] # 값이 3개 있고, 변수가 3개 있는 리스트 생성

# 2. 리스트의 사용 : 문자열 사용방식과 동등 + @가 생김
print(values1) # 보관된 것을 모두 보여주지만, 확인용으로만 사용한다.
print(values1[0], values1[-1])
values1[0] += 5
values1[-1] = "ApplePie"
print(values1)
# - 리스트는 어렵지 않음. "변수의 모양이 바뀌었음"을 잘 기억해야 함.

# 기본적으로 리스트가 적용된다면, 하나의 이름으로 변수 여러개가 관리되게 된다.
# - 이 때 하나의 이름으로 관리하는 기준은, "연관되어 있는 자료"인가 아닌가로 결정한다.
result = [0, 0, 0]
while result[0] <= 1:
    result[0] = int(input("정수 하나 입력 >> "))
num = 1
while num <= result[0]:
    if result[0] % num == 0:
        result[1] += num
        result[2] += 1
    num += 1
if result[2] != 2:
    result += ["참"]
else:
    result += ["거짓"]
print("%d로 구한 정보\n합 : %d, 수량 : %d개, 소수여부 : %s"%(result[0], result[1], result[2], result[3]))
print("약수목록")
num = 1
while num <= result[0]:
    if result[0] % num == 0:
        print(num, end=" ")
    num += 1
print()