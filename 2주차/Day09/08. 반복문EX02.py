# -100이상 100이하 => value >= -100 and value <= 100
# 이 조건식의 부정조건식은 뭘까요?
# - 부정연산자 : 조건식을 덜 고통받기 위해 쓴다.
value = -101
while not (value >= -100 and value <= 100):
    # 연산식이 중복되는 것처럼 보이지만, 값 자체가 다르기 때문에
    # 중복 연산이 아니다.
    value = int(input("-100 ~ 100 입력 >> "))
    if not (value >= -100 and value <= 100):
        print("재입력하세요.")
    

print("-100 ~ 100사이의 값 :",value)
