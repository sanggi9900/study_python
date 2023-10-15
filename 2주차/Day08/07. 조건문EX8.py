# 1) 같은거 빼기는 다 만들고 진행한다.
# 2) elif도 기본적으로 다 만들고 적용한다.
sc1 = int(input("국어 성적 >> "))
sc2 = int(input("영어 성적 >> "))
sc3 = int(input("수학 성적 >> "))
avg = (sc1 + sc2 + sc3) / 3
# 조건문 팁 : 제일 적은 경우의 수를 먼저 건다.
# - 걸러내는 구조를 만든다.
if avg >= 90:   rank = 'A'
elif avg >= 80: rank = 'B'
elif avg >= 70: rank = 'C'
elif avg >= 60: rank = 'D'
else:           rank = 'F'
# 다 만들고 나면 일반적으로 같은 것이 보인다.
print("평균 : %.2점\n등급 : %c등급"%(avg, rank))