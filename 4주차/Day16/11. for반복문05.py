# "목록" 처럼 보이는 것을 대상(객체)이 가지고 있는 값들을
# 왼쪽에서 오른쪽으로 차례대로 복사하여 꺼내주는 반복문

# while을 이용한 반복은, 대상 리스트에서 직접 인덱싱하여 가져온다.
lst = [1,2,3]   
index = 0
while index < len(lst):
    value = lst[index]
    print(value, end = ' ')
    index += 1
print()
# for를 이용한 반복은, 대상 리스트에 저장된 값을 무조건 복사한다.
lst = [1,2,3]
for value in lst:
    print(value, end = ' ')
print()