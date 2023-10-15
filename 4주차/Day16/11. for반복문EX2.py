# while로 리스트 생성후
lst = []
value = 1
while value <= 10:
    lst.append(value)
    value += 1
# for로 이를 활용한다.
print(lst)
for value in lst:
    print(value, end = ' ')
print()