# 조건문을 사용할 때 명심할 사항 : 같은 거 빼라.
num = int(input("정수 입력 >> "))
if num > 0:
    print("양수", end="")
    # result = "양수"
elif num < 0:
    print("음수", end="")
    # result = "음수"
else:
    print(num, end="")
    # result = str(num)
print("입니다.")
# 서식을 사용해도 좋습니다. 사용할 경우, 변수를 이용해서 빼내면 된다.
# print("%s입니다."%(result))