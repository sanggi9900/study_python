# 07. 조건문elif.py

num = int(input('정수 입력 >>> '))

if num == 1:        # 첫번째 조건
    print(1)

elif num == 2:      # 첫번째 조건이 False일때만 두번째 조건을 판단
    print(2)

elif num == 3:      # 첫번째와 두번째가 False일때만 세번째 조건을 판단
    print(3)

else:               # 이전에 등장한 모든 조건에 False일때 실행함
    print('1도 아니고 2도 아니고 3도 아님')

print('끝')