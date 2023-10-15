# 리스트 사용문제

# 이름과 국어/영어/수학 성적을 입력을 받습니다.
# 입력받은 성적으로 평균을 구합니다.
# 각각의 입력받은 값과 평균을 record 리스트에 저장하세요.
record = [ "이름", 0, 0, 0, 0 ]
record[0] = input("이름 입력 >> ")
record[1] = int(input("국어 성적 입력 >> "))
record[2] = int(input("국어 성적 입력 >> "))
record[3] = int(input("국어 성적 입력 >> "))
record[4] = (record[1] + record[2] + record[3]) / 3
print(record)

# 고려할 사항
# - 국어/영어/수학성적이 음수이거나 100점 초과하면 곤란합니다....
# - 집에서 추가로 한번 해보세요.
record = [ "이름", -1, -1, -1, 0 ]
record[0] = input("이름 입력 >> ")
while record[1] < 0 or record[1] > 100:
    record[1] = int(input("국어 성적 입력 >> "))
while record[2] < 0 or record[2] > 100:
    record[2] = int(input("영어 성적 입력 >> "))
while record[3] < 0 or record[3] > 100:
    record[3] = int(input("수학 성적 입력 >> "))
record[4] = (record[1] + record[2] + record[3]) / 3
print(record)