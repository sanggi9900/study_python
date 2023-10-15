# 리스트는 변수의 묶음 -> 값이 있으면 변수가 생성되고, 인덱스로 구분된다.
num1 = 10
num2 = 20
num3 = 30
lst = [ 10, 20, 30 ]
# 미리 준비될 요소가 있다면 준비하면 좋지만, 한도가 존재한다.
# -> 비어있는 곳에 값을 추가시켜 변수를 실시간으로 만들 수 있다.
lst1 = [10, 20, 30]
lst2 = []
lst1 += [40] # lst1 + [40]
print(lst1)
lst1 += [50] # lst1 + [50]
print(lst1, lst1[3], lst1[4])
lst2 += [1]
lst2 += [2]
lst2 += [3]
print(lst2)
print(lst2 * 2) # 새로운 변수를 만들면서 값을 복사하게 됨. # 잘 안씀

#  자료 -> 새로운 자료 -> 새로운 자료를 이용만 한다.
num = 11
value = 1
numLst = []
while value <= num:
    if num%value==0: numLst += [value]
    value += 1
print(numLst)
# 리스트의 크기를 구하여 약수의 수량을 해결한다.
count = len(numLst)
print("보관된 약수의 수량 :",count)
# 리스트에 보관된 값들만을 대상으로 반복을 수행한다.
# 1) 누적연산 구하기
result = 0
index = 0
while index < count: # index <= 3 -> index < 4
    result += numLst[index]
    index += 1
# 2) 보관된 값 출력하기
index = 0
while index < count: # index <= 3 -> index < 4
    print(numLst[index], end = " ")
    index += 1