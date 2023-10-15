# 숙제
# 표준 몸무게 공식
# 남성 : (키(cm) * 키(cm) * 22) / 10000
# 여성 : (키(cm) * 키(cm) * 21) / 10000

# 키를 입력을 받아, 이를 토대로 남성/여성 표준 몸무게를 출력하는
# 코드를 작성하세요.
# 출력형태는 자유롭게 하되, 소수점은 1자리까지만 나옵니다.
height = int(input("키 입력 >> "))
value1 = height ** 2
value2 = value1 * 21
form = "%s성 : %.1f KG"
print( form % ("남", (value2 + value1) / 10000))
print( form % ("여", value2 / 10000))
