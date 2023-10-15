# 4형식 : 완결된 코드(자료 -> 처리 -> 정보)
def program():
    num1 = int(input("정수1 입력 >> "))
    num2 = int(input("정수2 입력 >> "))
    result = num1 + num2
    print("두 정수의 합 :",result)
# 3형식 : 가장 가치가 있는 것이 외부로 복사되는 함수
def get_sum():
    num1 = int(input("정수1 입력 >> "))
    num2 = int(input("정수2 입력 >> "))
    result = num1 + num2 
    return result
# 2형식 : 자료를 복사받아서 이용하는 함수
# - 함수명은 show, print등의 표현이 사용된다.
# - 자료를 입력받아 저장하던 변수를 괄호 안에 배치한다.
#   이렇게 해주면, 호출할 때 넣어주는 값으로 함수에서 사용할 변수가 생성된다.
def show_sum(num1, num2):
    # 매개변수 : 외부로부터 값을 복사받아 생성되는 변수.
    #           외부 변수에 있는 값을 불러오는 용도가 절대로 아님
    result = num1 + num2
    print("두 정수의 합 :",result)

# 2형식의 주의사항 : 함수 내부에 있는 변수만 불러와야 된다.
def show_sum1():
    # 변수를 생성하면, 외부의 변수와 자동으로 구별이 된다.
    result = n1 + n2
    # 함수 내부에서 생성된 변수가 아니면
    # 자동으로 강제로 코드가 굴러가도록 맞춰버린다.
    print("두 정수의 합 :",result)
    # 매개변수가 없으면 값을 외부에서 받아올 수 없으니 주의
    
n1 = int(input("값1 입력 >> "))
n2 = int(input("값2 입력 >> "))
show_sum(n1 + n2, n1 * n2)
show_sum1()
# 함수 내부의 변수 num1 = 함수 외부의 변수 num1 + 함수 외부의 변수 num2
# 함수 내부의 변수 num2 = 함수 외부의 변수 num1 * 함수 외부의 변수 num2








# 3형식은 서로 다른 종류의 프로그램의 동일한 입력동작이 있으면 이에 적용한다.
# def get_int():
#     value1 = int(input("정수1 입력 >> "))
#     value2 = int(input("정수2 입력 >> "))
#     return value1, value2
# def program1():
#     values = get_int()
#     result = values[0] + values[1]
#     print("두 정수의 합 :",result)
# def program2():
#     values = get_int()
#     result = values[0] - values[1]
#     print("두 정수의 차 :",result)