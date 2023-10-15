members = {"kim611":"password1","Dong319":"password2"}

# 딕셔너리의 메서드 keys : 딕셔너리의 키만 뽑아낸다.
# 딕셔너리의 메서드 values : 딕셔너리의 값만 뽑아낸다.
id_list = members.keys() # members.values()
id_list = list(id_list) # 쓸 경우 형변환을 해줘야 한다.

id = input("ID >> ")
password = input("PW >> ")

# 멤버쉽연산자 in : A in B -> A가 B에 있는지 여부를 체크
flag = id in id_list
# 반복을 돌릴 수 있는 대상에 대해서, 알아서 반복돌려서 존재여부만 알려준다.

if flag:
    if members[id] == password:
        print("인증된 사용자 / 로그인 성공!")
    else:
        print("잘못된 비밀번호!")
else:
    print("회원 아이디가 없습니다.")