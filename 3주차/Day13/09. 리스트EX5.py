lst = []
lst += [int(input("1번 값 >> "))]
lst += [int(input("2번 값 >> "))]
lst += [int(input("3번 값 >> "))]
lst += [int(input("4번 값 >> "))]
lst += [int(input("5번 값 >> "))]

print("초기상태 리스트 :",lst)
lst[1:2] = []
print("1번 제거 리스트 :",lst)
lst[1:1 + 2] = [] # [ 시작위치 : 시작위치 + 수량 ]
print("1~2번 구간 제거 리스트 :",lst)