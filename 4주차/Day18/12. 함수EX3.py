# 4형식 -> 2형식
# - 입력받은 것을 몽땅 쳐내고 매개변수로 올리는 것
def show_bigger(num1 , num2):
    if num1 == num2:
        print("서로 같은 값 :",num1)
    else:
        print("제일 큰 값 : ", end = ' ')
        if num1 > num2:
            print(num1)
        else:
            print(num2)
# 2형식일 경우
show_bigger(15,4)
show_bigger(4,15)
show_bigger(4,4)
# - 값을 호출할 때 넣어주면 왼쪽부터 오른쪽으로 전달된다.