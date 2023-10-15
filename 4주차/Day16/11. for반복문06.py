# for문은 항상, 유한반복만 가능하다.
# - 유한반복이면 어디에든 적용이 가능하다
# for의 단점 : "목록"을 직접 준비하는 과정이 필요하다
# - 일반적으로 입력받을 때는 while로 통제하고...
# - 일반적으로 완성된 것을 쓸 때는 for를 이용한다...

# 결국 "목록"만 빠르게 준비하면 된다!
# -> range()를 이용하여 빠르게 준비한다.

# range() : 정수 리스트 비스무리한 것을 준비해준다.
# 1) range(A) : 0부터 A-1까지의 정수를 준비 / A번만큼 반복
for x in range(5): # 단순반복횟수 설정용
    print("WOW~", end = ' ')
print()
lst = ['A','B','C','D']
for i in range(len(lst)): # 인덱싱에 투입한다.
    print( lst[i], end = ' ' )
print()

# 2) range(A, B) : A부터 B-1까지의 정수를 준비 / B-A번만큼 반복
# ※ B는 반드시 A보다 커야 한다. A와 같거나 A보다 작으면 깡통이 나온다.
# - 특정 범위의 1씩 증가하는 정수가 필요할 때 사용한다.
for count in range(11,16):
    print("%d번째 출력!"%(count))

# 3) range(A,B,C) : A부터 B미만/초과 범위의 C만큼 변하는 정수를 준비
# - 특정 규칙을 가진 숫자들을 준비하는게 목적
# - C > 0이면, A < B일 경우에만 정수목록이 나온다.
# - C < 0이면, A > B일 경우에만 정수목록이 나온다.
# - C == 0이면, 에러가 발생한다.
print(list(range(1,6,2))) # A부터 B-1까지(미만)
print(list(range(6,1,-2))) # A부터 B+1까지(초과)
for num in range(1,100): # 모든 숫자를 골라내는 것보다
    if num % 2 != 0:
        print(num, end = ' ')
print()
for num in range(1,100, 2): # 이게 더 효율적이고 맞는 코드다.
    print(num, end = ' ')
print()