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
def show_sum(num1, num2):
    result = num1 + num2
    print("두 정수의 합 :",result)
# 1형식 : 자료를 외부에서 복사받아 정보를 외부로 복사시켜주는 함수
# - 내부에서 print를 할 일이 없음.
# - make,create,convert 등등.. 만들어내는 표현이 많이 붙는다.
def make_sum(num1, num2):
    result = num1 + num2
    return result

# return이 있을 경우, 여러번 쓰면 저장한다.
result = make_sum(10,30)
print(result)

# 한번 쓰면 필요한 곳에 바로 작성한다.
print(make_sum(11,31))

# 연산식에 바로 적용해도 됨
new_result = result + make_sum(1,3)
print(new_result)