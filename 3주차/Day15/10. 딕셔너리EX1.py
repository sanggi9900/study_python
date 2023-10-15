myinfo = {}
myinfo["이름"] = input("이름 입력 >> ")
myinfo["나이"] = int(input("나이 입력 >> "))
myinfo["취미"] = input("취미 입력 >> ")
print("개인정보")
print(myinfo)

# 딕셔너리는 while으로는 반복을 운용할 수 없음
# - 목록이 준비되어 있는 리스트가 있어야 되고, 이를 반복하여 운용한다.
myinfo = {}
items = ["이름","나이","취미"]
index = 0
while index < len(items):
    myinfo[ items[index] ] = input( items[index] + " 입력 >> " )
    index += 1
myinfo["나이"] = int(myinfo["나이"])
print("개인정보")
index = 0
while index < len(items):
    print(myinfo[ items[index] ], end = ' ')
    index += 1
print()