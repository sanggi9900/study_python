# 1. 직관적으로 판단할 경우
# 10부터 1까지 1씩 감소한다. 출력한다.
num = 10
while num >= 1:
    print("%.2d"%(num), end=" ")
    num -= 1 # num += -1
print()

# 2. 직접 작성해서 분석하는 방법
# 11부터 20까지 1씩 증가한다. 출력한다.
# 1) 단순 코드로 작동하는 내용을 작성한다.
# 2) 같은 형태의 코드가 나오도록 분해한다.
# 3) 변수와 연산식을 이용해 상수를 걷어낸다.
# 4) 끝을 파악하고, 반복문으로 포장한다.
num = 11
while num <= 20:
    print(num, end=' ')
    num += 1
print()
