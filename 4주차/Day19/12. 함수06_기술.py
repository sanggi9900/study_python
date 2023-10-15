# 1. 기본값(Default Arguments)
# - 함수가 사용되면서, 자주 사용되는 상수값이 있으면 이를
#   미리 넣어두는 것
# - 매개변수에 적용되며, 항상 오른쪽부터 채워야 된다.
#   상수값이 아닌 것은 절대 넣지 말 것
def function1(n1, n2 = 15, n3 = 30):
    print(n1, n2, n3)
function1(10,20) # 함수 호출시에 자주 사용되는 가장 오른쪽 상수값을
function1(11,21) # 매개변수의 해당 자리에 넣어두는 것
function1(15,26,31) # 새로운 값을 넣었을 경우, 해당 값으로 작동한다.
function1(31)
function1(1)

# 2. 위치기반 전달인자(Positional Arguments)/키워드기반 전달인자(Keyword Arguments)
# - 튜플 / 딕셔너리를 매개변수로 준비한다.
# - 매개변수의 수량이 불특정이고, 값의 수량도 불특정이고, 함수의 사용방식이 정해지지 않음

def posArg(*values): # 적용할 변수에 *를 붙여 준비
    for value in values:
        print(value, end=' ')
    print()
posArg(1,2,3,4,5,6,7,8,9)
posArg(1,2,3,4,5)
posArg(*[10,20,30]) # 해당 매개변수가 있다면 *를 붙여 전달 가능

def kwdArg(**values): # 적용할 변수에 **를 붙여 준비
    print(values)
    if 'A' in values:
        print(values['A'])
    if 'B' in values:
        print(values['B'])
    if 'C' in values:
        print(values['C'])
kwdArg(A=100,B=200,C=300) # 값을 순서가 아닌 이름으로 구별해서 사용해야 할 때 적용
kwdArg(B=200,C=300,A=100)
kwdArg(**{'A':1,'B':2})