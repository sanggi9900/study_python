# 내장모듈 : 파이썬 설치과정에서 같이 포함된 모듈들
# - 1. Python Module Docs를 이용해야 한다.
#     단, 기술적으로 어려운 내용이 상당히 많이 적혀 있음
# - 2. 파이썬 공식문서를 이용해야 한다.
#     한글로 잘 번역되어 있고, 예시도 함께 있기 때문에 참고 가능
# - 3. 외장 모듈은 모듈명 + Manual형태로 구글에 검색해야 한다.
#     인지도 좋은 모듈은 공식사이트, 예시, 문법 등을 제공한다.

# 의사난수모듈 random
import random
# randint(A,B) : A <= X <= B인 X값을 반환하며, 정수값이다.
# - 호출할 때마다 새로운 값이 나온다.
value = random.randint(1,45)
print(value) # 함수를 호출해야만 값이 바뀜
print(value)
# choice(목록) : 목록중에서 임의의 하나(값)를 골라서 반환한다.
# dic1 = {'A':1,'B':2,'C':3} # 딕셔너리는 불가
# print(random.choice(dic1)) # 리스트로 형변환시켜서 투입시켜야 함
lst1 = [10,20,30,40]
word = "ABCDEFG"
# 기본적으로 인덱스가 존재하는 것만 가능
print(random.choice(lst1))
print(random.choice(word))