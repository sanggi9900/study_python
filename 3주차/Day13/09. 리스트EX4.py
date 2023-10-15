lst = []
lst += [input("값1 입력 >> ")]
lst += [input("값2 입력 >> ")]
lst += [input("값3 입력 >> ")]
# 인덱싱할 경우 주의사항
# - 문자열은 문자열이 나온다
# - 리스트는 리스트가 나오지 않고, 해당 위치의 값이 나온다.
#   해당 값의 종류에 따라서 인덱싱한 값의 종류도 바뀐다.
print("원본리스트")
print(lst)

# new_lst1 = [lst[2], lst[1], lst[0]]
new_lst1 = []
index = 2 # len(lst) - 1 # 마지막 인덱스는 언제나 전체수량 -1 이다.
while index >= 0:
    new_lst1 += [lst[index]]
    index -= 1

print("순서를 뒤집어 새로 만든 리스트")
print(new_lst1)

new_lst2 = new_lst1 + lst
print("원본과 순서를 뒤집은 리스트를 합친 리스트의 첫번째와 마지막")
print(new_lst2)
print(new_lst2[0], new_lst2[-1])