num = float(input("숫자 입력 >> "))
if num > 0:
    print("연산결과 :",num * 5)
elif num < 0:
    print("연산결과 :",num / 5)
else:
    print("연산할 대상이 없습니다.")
# 항상 고려할 사항 : 같은거 빼라.
# - elif는 만능이 아니다.
# - elif는 if/else로 코드 만들고 나서 적용하는게 베스트.
if num == 0:
    print("연산할 대상이 없습니다.")
else:
    print("연산결과 : ", end="")
    if num > 0:
        print(num * 5)
    else:
        print(num / 5)
