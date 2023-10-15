# 10보다크고 100보다 작다
num = 0
while not (num > 10 and num < 100):
    num = int(input("범위내의 정수 입력 >> "))
    if num <= 10:
        print("%d는 11보다 %d만큼 작습니다."%(num, 11 - num))
    if num >= 100:
        print("%d는 99보다 %d만큼 작습니다."%(num, num - 99))

print("10보다 크고 100보다 작은 값 :", num)