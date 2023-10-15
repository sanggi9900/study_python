# 딕셔너리의 제일 큰 목적 
# - 저장되는 것들을 정확하게 이름으로 구분한다.
# - 리스트였다면, id 리스트와 패스워드 리스트가 따로 준비되고
#   이는 각각 인덱스에 의해서 구별된다.
members = {"kim611":"password1","Dong319":"password2"}
id = input("ID >> ")
password = input("PW >> ")
if members[id] == password:
    print("인증된 사용자 / 로그인 성공!")
else:
    print("잘못된 비밀번호!")