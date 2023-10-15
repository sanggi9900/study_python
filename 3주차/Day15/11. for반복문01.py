members = {"kim611":"password1","Dong319":"password2"}
# id를 체크할려면 리스트가 필요하다
id_list = ["kim611", "Dong319"]
id = input("ID >> ")
password = input("PW >> ")
index = 0
flag = False
while index < len(id_list):
    if id == id_list[ index ]:
        flag = True
        break # 보조제어문. 반복문을 보조하기 위한 예약어
        # 반드시 조건문과 써야 한다.
    index += 1

if flag:
    if members[id] == password:
        print("인증된 사용자 / 로그인 성공!")
    else:
        print("잘못된 비밀번호!")
else:
    print("회원 아이디가 없습니다.")