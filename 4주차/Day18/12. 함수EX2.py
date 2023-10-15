# ※ 함수 만들 때 팁
# - 4형식으로 함수를 먼저 만들고...
#   제일 가치가 있는 것을 출력 대신에 return처리하면, 3형식이 된다.
def get_sum():
    num = int(input("정수 하나 입력 >> "))
    result = 0
    # while 유한반복 -> 변수를 갈아마신다.
    result = 0
    while num >= 1:
        result += num
        num -= 1
    return result

result = get_sum()
print("함수에서 구한 합 :", result)




# for로 합을 구할 경우
def get_sum_for():
    num = int(input("정수 하나 입력 >> "))
    result = 0
    # for 유한반복 -> 변수를 온전하게 유지한다.
    for i in range(1, num+1): # range(num, 0, -1):
        result += i
    return result