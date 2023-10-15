members = {"kim611":"password1","Dong319":"password2"}
id = input("ID >> ")
password = input("PW >> ")

# 멤버쉽연산자 in은 "목록" 있으면 바로 이용할 수 있다.
# - 목록은 형변환을 거치면 리스트가 되고, 이를 반복 돌려서 처리해준다.
# - 문자열 / 리스트 / 튜플 / 딕셔너리 / 딕셔너리의 부산물 등...
if id in members:
    if members[id] == password:
        print("인증된 사용자 / 로그인 성공!")
    else:
        print("잘못된 비밀번호!")
else:
    print("회원 아이디가 없습니다.")