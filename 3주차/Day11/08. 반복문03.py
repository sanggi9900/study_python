# 누적하기 : 반복문 활용의 기초이자 기본이자 모든 것
# - 코드는 실시간으로 바꿀 수 없다.
# 누적의 경우, 대부분의 경우 연산이다.
# - 연산의 특징 : 대부분의 경우 이항연산이다.
# case 1. 숫자
result = 0
num = 1
while num <= 15:
    result += num
    num += 1
print(result)

# case 2. 문자열
# result = "" # 문자에서는 비어있는 문자값이 준비가 된다.
result = "%c"%(0) # 정수 0 -> 문자값 '비어있음(NUL)'을 의미합니다.
num = 1
while num <= 15:
    result += "%c"%(num + 64)
    num += 1
print(result)

# case 3. 출력
num = 1
while num <= 15:
    # "화면"도 저장공간이다. print를 통해 화면상에 특정 형태의 문자들을
    # 누적하여 우리는 의사소통을 할 수 있다.
    print(num, end = ' ')
    num += 1
print()