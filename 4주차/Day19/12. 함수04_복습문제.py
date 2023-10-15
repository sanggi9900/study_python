# 4형식 문제
# - 내가 입력한 구간에 있는 1씩 증가하는 정수를 모두 출력하는 함수를
#   정의하여 호출하세요.
def main_program():
    n1 = int(input("시작값 입력 >> "))
    n2 = int(input("끝값 입력 >> "))
    if n1 <= n2:
        for i in range(n1, n2 + 1):
            print(i, end=' ')
        print()
    else:
        print("구간이 맞지 않습니다.")
# 3형식 문제
# - 내가 입력한 구간에 있는 정수들을 리스트에 담아 반환하는 함수를
#   정의하여 호출하세요.
def getNumLst():
    n1 = int(input("시작값 입력 >> "))
    n2 = int(input("끝값 입력 >> "))
    if n1 <= n2:
        return list(range(n1, n2 + 1))
    else:
        return []
# 2형식 문제
# - 임의의 리스트에 저장된 값들을 모두 출력하는 함수를 정의하세요.
def showLst(lst):
    if lst == []:
        print("리스트가 깡통이네요.")
    else:
        for i in lst:
            print(i, end=" ")
        print()

# 4형식 코드
main_program()
# 3형식 코드
lst = getNumLst()
print("결과 :",lst)
# 2형식 코드
any_lst = [1,2,3,'A','B','C',3.1,3.2,3.3]
showLst(any_lst)