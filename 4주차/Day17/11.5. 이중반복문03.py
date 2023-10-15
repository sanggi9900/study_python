# 3. 무한 + 유한 - 입력받은 것을 판별할 때
# -> 입력받은 값의 종류를 판별하여 형변환한다.
mychoice = "문자"
while True:
    value = input("값 입력 >> ")
    numlst = ['0','1','2','3','4','5','6','7','8','9','.']
    flag1 = True
    for ch in value: # 1. 숫자와 숫자가 아닌 것( 123 / 3.14 vs 그 외의 것 )
        if ch not in numlst: # 입력받은 문자열의 문자들을 모두 체크
            flag1 = False
            break
    if not flag1:
        print("문자값 :",value) 
        result = "문자"
    elif value.count('.') > 1: # 문자열 메서드 count : 특정문자의 수량을 세어 알려준다. 최소 0.
        print("문자값 :",value)
        result = "문자"
    elif value.count('.') == 1: # 2. 숫자 중에서 정수/실수인지 여부
        print("실수 형태의 문자값 :",value)
        result = "실수"
    else:
        print("정수 형태의 문자값 :",value)
        result = "정수"
    if result == mychoice:
        break
    