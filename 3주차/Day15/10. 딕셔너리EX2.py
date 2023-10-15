myinfo = {}
# 반복을 구성할 경우, 최대한 통일된 코드가 되도록 만들어야 한다.
myinfo["이름"] = input("이름 입력 >> ")
myinfo["나이"] = int(input("나이 입력 >> "))
myinfo["취미"] = input("취미 입력 >> ")
myinfo["목표"] = input("목표 입력 >> ")
myinfo['A'] = input("아무값1 입력 >> ")
myinfo['B'] = input("아무값2 입력 >> ")

# 반복 돌릴 수 없으면, 변수의 묶음 중 특정 변수를 이용해, 저장된 값을
# 불러와서 써야 한다.
print( "이름 :",myinfo["이름"] )
print( "나이 : %d세"%(myinfo["나이"]) )
print( "취미 :",myinfo["취미"] )
print( "목표 :",myinfo["목표"] )
print("A -",myinfo['A'])
print("B -",myinfo['B'])

# ☆ 딕셔너리의 key는 저장된 값들을 구별하는 고유명칭이다.