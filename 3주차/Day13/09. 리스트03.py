# 리스트는 언제나, 내부에 값들이 보관되고, 이를 쓰는 것이 목적
# - 값들의 추가 및 서로 다른 리스트들의 합치기도 자유롭다.
# - 연관되어 있는 것들이기 때문에 합쳐서 운용한다.

# 문자열의 슬라이싱과 똑같이, 리스트도 슬라이싱이 가능하다.
name = "홍길동"
print(name[0:1], name[1:3])
# - 전체 값들 중에서 필요한 것들만 이용하기 위한 것
#            0    1  2  3  4  5
record = [ "Tom",98,93,97,73,28 ]
#         0     1  2  3  4  5  6
result = 0
scores = record[1:6] # record[1 : 1 + 5]
print(scores)
num = 0
while num < len(scores):
    result += scores[num]
    num += 1
print(result)
