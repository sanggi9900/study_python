# for 반복문은 목록이 있어야만 반복가능
# - 값이 없는 목록은 반복을 하지 않는다.

int_list = []
# 4번 무조건 입력을 받지만, 중간에 끝날 수 있음
# count = 1
# while count <= 4:
#     value = int( input( str(count)+"번 정수 >> " ) )
#     if value != 0:
#         int_list.append(value)
#     else:
#         break
#     count += 1
# ※ 구간주석 단축키 : 드래그 후 ctrl + k + c(적용), u(해체)

# 무한 반복이면 0 이외의 값만 저장하면 된다.
count = 1
value = 1
while value != 0:
    value = int( input( str(count)+"번 정수 >> " ) )
    if value != 0:
        int_list.append(value)
    count += 1

# ☆ 리스트에 저장된 값의 수량이 바뀌어도 알아서 처리해주고
#   알아서 판단해준다.
print("리스트에 저장된 값들")
for value in int_list:
    print(value, end = ' ')
# ★ for제어문의 핵심포인트는, 종속문에서 무엇을 할 것인지
#   의도를 명확하게 담아야 한다.
result = 0
for value in int_list:
    result += value
print("\n저장된 값들의 합 :", result)