# 산술연산자 : "기본적으로" 수치연산에 이용되는 연산자

count = 10
# 1. 변수는 많이 만들어서 좋은 점이 없다.
#   한번 밖에 안쓴다면, 1회성 가치밖에 없다는 것과 같다.
print(count,"- 3 =", count - 3)
print(count,"+ 3 =", count + 3)

# 2. 특정 연산이 많이 사용된다면, 다회성이고....
#   다회성의 연산결과는 엄연한 정보/새로운 자료로써 이용해야 된다.
#   기준은, 2회이상 사용되는가? 로 판단한다.
#   - 다회성 여부와 관계없이, 기존 연산결과를 보존하기 위해 사용하기도 한다.
value = count * 5
print("result1 :", value)
count = 8
print("result2 :",value,"vs",count*5)

# 규칙 : 실수와 나누기를 조심해라
print("result3 :",count * 2.5) # 정확한 배수라는 개념이 없고
print("result4 :",count / 2) # 나누어 떨어진다는 개념이 없음
# 몫과 나머지는 나눗셈으로 만들기 어려운 것을 쉽게 만들어준다.
count = 100
print("result5 :",count // 3) # 100개를 3개씩 뿌리면 33회 뿌릴 수 있다.
print("result6 :",count % 3) # 100개를 3개씩 뿌리면 마지막엔 1개가 남는다.
print("result7 :",count / 3) # 100개를 3개씩 뿌리면 33.33회 가능하다.

# 거듭제곱은 곱셈 귀찮아서 쓴다. 2번 이상이면 쓰면 된다.
print("result8 :",count*count*count*count)
print("result9 :",count**4)