# 프로그램에서 자료는 필요한 경우에만 중간에 입력을
# 받아서 보충하고, 그런게 아니라면 모두 다 받고 진행된다.

# - 입력구간 : 프로그램에 필요한 자료를 모두 수집하는 과정
name = input("이름을 입력하세요 >> ")
age = input("나이 입력하세요 >> ")
hobby = input("취미를 입력하세요 >> ")

# - 출력구간 : 처리를 거치고 만들어지는 결과물을 출력하는 과정
print("내 이름은",name,"입니다.")
print("내 나이는",age,"세이며")
print("취미는",hobby,"입니다.")

# 요령 - 먼저 나오게 하고 싶은 것을 상수로 작성한다.
print("취미는 코딩 입니다.")
print("취미는","코딩","입니다.")
print("취미는",hobby,"입니다.")