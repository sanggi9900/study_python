# 유한 + 무한 실습문제
# 실수값 5개를 입력을 받아 리스트에 보관합니다.
# 단, 실수값의 실수부가 반올림할 수 없는 값일 경우
#    재입력을 받습니다.
# 반올림이 가능한 실수값 5개가 보관된 리스트를 출력하세요.
lst = []
# 다중 반복문은 종속코드를 그대로 반복시켜 작동시켜주는 코드에 불과하다.
for i in range(1, 6):
    value = 0.4
    while value - int(value)<0.5: # value % 1 < 0.5
        value = float( input( "실수값%d 입력 >> "%(i) ) )
    lst.append(value)
print(lst)

# while 단일반복 + continue로 조합하여 처리 가능
# 팁 : continue 및 break를 쓸 경우, 안쓰고 만들었을 때 도저히 답이 안나오면
#     그 때 추가해보자
lst = []
num = 1
while num <= 5:
    value = float( input( "실수값%d 입력 >> "%(i) ) )
    if value - int(value) >= 0.5:
        lst.append(value)
        num += 1
print(lst)