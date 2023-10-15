lst = []
# "회" 빼고 슬라이싱해서 형변환하면 된다.
limit = int( input("횟수 입력 >> ")[ : -1 ] )
count = 1
while count <= limit:
    value = int( input( "%d번 정수 >> "%(count) ) )
    lst.append( value )
    count += 1
print(lst)

index = 0
result = 0
# 크기가 5일 경우, 0 ~ 4번 인덱스까지만 있다.
# 마지막 인덱스는 언제나 전체 크기 - 1이다.
while index < len(lst): # 정수에 한해서, X <= 5 - 1 와 X < 5은 같은 표현이다.
    result += lst[index]
    index += 1
print("합 :", result)