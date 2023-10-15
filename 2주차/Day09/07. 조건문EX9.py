# 조건문 복습문제

# 주차시간을 입력을 받아 주차요금을 출력하는 코드를 작성하세요.
# 1) 주차시간은 30분이하 이면 <무료>
# 2) 30분초과 60분이하 이면 <3000원>
# 3) 60분을 초과하면 초과한 시간을 10분단위로 계산해
#    3000원에 500원씩 더합니다.
# 4) 예외인 경우의 수는 <잘못된 입력>으로 출력합니다.
time = int(input("주차시간 >> "))
if time < 0:
    print("잘못된 입력!")
else:
    if time <= 30:
        result = "무료"
    elif time <= 60:
        result = 3000
    else:
        # 조건연산자 A if 조건식 else B
        # - 조건식이 참일 때는 A, 거짓이면 B를 사용
        # - 값만 골라낼 때 쓴다.
        add_value = ((time-60)//10) + 1 if time % 10 !=0 else 0
        # add_value = ((time-60)//10) + 1
        # if time % 10 != 0:
        #     add_value += 1
        # else:
        #     add_value += 0
        result = 3000 + add_value * 500
    print("요금 :",result)
