lst = []
lst += [input("값1 입력 >> ")]
lst += [input("값2 입력 >> ")]
lst += [input("값3 입력 >> ")]
print(lst)

# 리스트를 쓸 때는 많은 경우, 항상 반복이 따라온다.
# -> 개별 인덱싱하는 경우는 별로 없음
# -> 개별 추가도 별로 없음
# -> 항상 반복에 의하여 특정 순번/순서/수량을 처리하도록 만든다.
lst = []
num = 1
count = int(input("입력횟수 >> "))
while num <= count:
    lst += [input("값%d 입력 >> "%(num))]
    num += 1
print(lst)
# ※배수는 특정 순번에 있는 것들만 확인할려고 할 때 이용하는 규칙이다.
num = 0
while num < count:
    print(lst[num])
    num+=2