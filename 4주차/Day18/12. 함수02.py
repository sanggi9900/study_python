# 4형식 : 완결된 코드(자료 -> 처리 -> 정보)
# - 코드 정리용도 / 프로그램 내부에 별개 프로그램들을 준비할 때
# - 소스파일에 섞여 있으면 코드 관리가 안된다!
def program():
    num1 = int(input("정수1 입력 >> ")) # 자료
    num2 = int(input("정수2 입력 >> "))
    result = num1 + num2                # 처리
    print("두 정수의 합 :",result)       # 정보

# 3형식 : 가장 가치가 있는 것이 외부로 복사되는 함수
# - 변수는 절대로 복사되지 않는다.
# - 변수에 저장된 값은 복사될 수 있음.
# ※ 3, 2, 1형식은 모두 동사로 함수명을 설정한다.
# - 3형식은 get, input, put 등의 표현이 많이 사용된다.
def get_sum():
    num1 = int(input("정수1 입력 >> ")) # 자료
    num2 = int(input("정수2 입력 >> "))
    # return : 지정한 대상을 함수가 사용된 곳에 복사시켜주는 명령어
    #          + 함수의 종료를 담당
    result = num1 + num2                # 처리

    # 1. return은 연속사용할 수 없지만, 조건문으로 선택 가능
    return result
    # 2. return을 통해서 여러개의 값이 나오도록 할 수 있다.
    # - 쉼표로 구분만 하면 튜플로 묶어준다.
    # - 또는 리스트 등으로 직접 묶어줄 수 있다.
    # return num1, num2, result -> return (num1, num2, result) 를 의미한다.
    # return [num1, num2, result]

# return이 있을 경우 변수 오른쪽에 올 수 있다. 변수와 유사하게 사용됨.
result = get_sum()
print("결과 :", result)