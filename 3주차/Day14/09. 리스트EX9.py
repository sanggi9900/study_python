lst = []
limit = int( input("횟수 입력 >> ")[ : -1 ] )
count = 1
# 유한반복과 무한반복은 합칠 수 없다.
if limit == 0:
    value = -1
    while value != 0:
        value = int( input( "%d번 정수 >> "%(count) ) )
        if value != 0:
            lst.append(value)
        count += 1
else:
    while count <= limit:
        value = int( input( "%d번 정수 >> "%(count) ) )
        lst.append( value )
        count += 1






        
index = 0
result1 = 0
result2 = 0
while index < len(lst):
    if lst[index] > 0:
        result1 += lst[index]
    else:
        result2 += lst[index]
    index += 1
print("양수합 :", result1)
print("음수합 :", result2)