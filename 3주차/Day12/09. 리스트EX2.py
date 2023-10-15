lst = [
    123,    # 필요시 줄바꿈해서
    456,    # 정리할 수 있음
    3.14,   # 이런 모양으로
    9.12,   # 저장되는 것은 아님
    "Apple",
    "Pie",
    True,
    False
    ]
# 리스트를 사용함으로써 얻는 이점 : 개별 변수들 및 값을 하나의 이름과 순번(인덱스)으로 관리한다.
# 리스트를 사용함으로써 얻는 약점 : 변수들을 잘 구별해야 한다.
# 별 차이가 없는 사항 : 결국 변수 모양만 바뀌었을 뿐이다.
print("합 :", lst[0] + lst[1])

result = "%.2f"%(lst[2] * lst[3])
print("곱결과 :", result, end="")
print(" / 정수부 :", result[ : result.find('.')] , end="")
print(" / 실수부 :", result[ result.find('.')+1 : ] )

print(lst[4] * 2 + lst[5] * 2)

print("참 :",lst[-2])

print("거짓 :",lst[-1])


# round(실수값, 반올림자릿수)
print("곱결과 : %.2f"%(lst[2] * lst[3]),end="")
print(" / 정수부 :", int(lst[2] * lst[3]), end="")
print(" / 실수부 :", int(round((lst[2] * lst[3]) % 1, 2)*100))