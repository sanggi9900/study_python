def change(num):
    if num % 2 == 0:
        return num + 1
    else:
        return num - 1
print("결과1 :", change(13))
print("결과2 :", change(16))
print("결과3 :", change(-16))
print("결과4 :", change(-13))