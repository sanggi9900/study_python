# up & down 코드를 만들어보세요.
# 적당한 값을 기준으로 하여
# 이보다 크면 down, 이보다 작으면 up
# 정확하게 적당한 값을 입력했으면
# 정답이라고 출력하도록 코드를 정의하세요.
# 정답을 맞추지 못하는 경우의 수는 없습니다.
quiz_answer = 30
value = 29
while quiz_answer != value:
    # 입력전에는 30이 아닌 경우의 수만 들어온다.
    if value > quiz_answer:
        print("변화전 : UP!")
    else:
        print("변화전 : DOWN!")
    value = int(input("UP & DOWN >> "))
    # 입력후에는 30이 아니라고 확정할 수 없음.
    if value > quiz_answer:
        print("변화후 : UP!")
    elif value < quiz_answer:
        print("변화후 : DOWN!")

print("정답입니다.")