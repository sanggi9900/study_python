# 2. 유한 + 무한 : 입력시에 제일 많이 사용되는 조합중 하나
# - 과목 3개의 점수를 입력받는다.
score_dic = {"국어":-1, "영어":-1, "수학":-1}
print(score_dic)
print(list(score_dic))
for subject in score_dic:
    while score_dic[subject] < 0 or score_dic[subject] > 100:
        score_dic[subject] = int(input(subject + "점수 입력 >> "))
print(score_dic)
# 1) 정해진 수량의 값이 필요하고
# 2) 이를 걸러내어 받아야 할 때
