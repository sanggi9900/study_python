# 모듈(module) : 기본 함수 외에 추가 함수를 불러오는 문법
# time 모듈 : 시간과 연관된 기능이 들어있음
import time
# time함수 : 1970년 1월 1일부터 누적된 초단위시간을 출력
print(time.time())
# 활용 : 시작시간과 끝시간을 저장해 빼주면 소요시간이 나온다.

# 팁 : for문의 변수는 1회용으로 간주한다.
# - 중복되도 상관없는 변수명/단문자(i)로 설정한다.
for i in range(1, 11): # range(1,11,1)
    print(i, end = ' ')
print()
for i in range(11, 100, 11):
    print(i, end = ' ')
print()
for i in range(96, 7, -8):
    print(i, end = ' ')
print()
# while반복보다 최대 2배까지 더 빠른 속도로 작동한다.