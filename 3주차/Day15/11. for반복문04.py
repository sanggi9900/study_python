# for : 멤버쉽연산자의 내부처리과정을 반대방향으로 뒤집은 제어문
# a in b
# -> 대상 b를 리스트로 바꿔서 내부에 있는 것을 인덱싱해서 a와 같은지 체크
word = "ABC"
tup = ( 1, 2, 3 )
lst = [ 10, 20, 30 ]
dic = { 'A':1.1, 'B':2.2, 'C':3.3 } # 딕셔너리는 key만 체크한다.
print('A' in word, 1 in tup, 11 in lst, 3.3 in dic)

# for문의 장점 : while기반 숫자놀음보다 좀 더 직관적으로 사용가능
# - 목록이 있으면 왼쪽에서 오른쪽으로 무조건 진행한다.
# - 유한반복에 특화되어 있음

# for a in b
# -> b 내부에 있는 것들을 하나씩 순서대로 a에 계속 복사하며 반복을 진행
# 문자열 - 문자 하나씩 자동 인덱싱한다.
print(list(word))
for ch in word:
    print(ch, end=' ')
print()
# 튜플 / 리스트 - 애초에 인덱스가 있으니, 자동 인덱싱한다.
for value1 in tup:
    print(value1, end = ' ')
for value2 in lst:
    print(value2, end = ' ')
print()
# 딕셔너리 - 키만 나오기 때문에, 키를 다시 이용해야 값을 볼 수 있다.
print(list(dic))
for key in dic:
    print(key, dic[key])

# 주의사항 : 무한반복 절대 불가