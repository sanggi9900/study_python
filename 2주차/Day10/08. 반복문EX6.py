ch = 65
while ch <= 90:
    print("%c"%(ch), end="")
    ch += 1
print()

# 문자열은 인덱싱이 되고, 인덱싱은 정수이기만 하면 된다.
# ☆ 인덱싱은 대부분의 경우 처음부터 시작한다.
num = input("정수 입력 >> ")
i = 0
flag = True
while i < len(num): # 다중반복 : 반복문 내부에 반복문이 존재하는 구조
    ch = 65
    while ch <= 90: # - 내부의 반복이 다 끝나야 외부의 1회가 끝난다.
        if num[i]=="%c"%(ch):
            flag = False
        ch += 1
    i += 1
if flag:
    print("정상적으로 형변환 가능! ->", int(num))
else:
    print("형변환하면 안됩니다!!!!", num)