scores = []
# 입력에 대한 반복은 "반복횟수"에 집중하거나 새로운 리스트를 만든다.
# 1) 반복횟수 - 숫자를 준비하여 돌린다.
# count = 1
# while count <= 7:
#     scores += [ int( input( "%d번 성적 >> "%(count) ) ) ]
#     count+=1

# 2) 리스트를 만들기 - 규칙성을 만들어낼 수 없으면 목록을 만든다.
subject = ["국어", "영어", "수학", "사회", "과학", "음악", "도덕"]
index = 0
while index<=6:
    scores += [ int( input( subject[index] + " 성적 >> " ) ) ]
    index += 1

# 만들어진 리스트의 사용은 정수 숫자 놀음이다.
# - 숫자들만 반복문으로 준비해서 이용하면 된다.
# - 숫자들을 효율적으로 준비하면, 리스트도 효율적으로 운용된다.
sum_score = 0
index = 0
while index<=6:
    sum_score += scores[index]
    index+=1
print(sum_score)

index = 0
while index <= 6:
    print(scores[index], end=' ')
    index += 1
print()