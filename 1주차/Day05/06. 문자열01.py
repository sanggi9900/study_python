# 문자값은 우리의 기본적인 언어에 대한 인식을 기반으로 한다.
# Apple + Pie = Apple Pie

# ☆ 변수는 늘어봤자 좋은 것은 전혀 없다.
# 합치기는 변수를 줄여주고, 연산자사용의 기본규칙을 달성한다.
fruit1 = "Apple"
dish1 = "Pie"
# - 이것이 보관되는 용도(File / Data Base)라면 달라진다.
print(fruit1, dish1)
# - 개별 보관보다 하나로 합쳐 보관하는 것이 효율적이다.
cook1 = fruit1 + " " + dish1
print(cook1)
# - 융통성이 엄청 좋기 때문에, 규칙만 잘 부과한다면, 온갖 정보를 붙일 수 있다.
count = 5
cook1 += " <" + str(count) + "개>"
print(cook1)

# 반복하기는 여러번 + 연속사용의 피로를 줄여준다.
print("==================================================================")
print("이전 내용과 구별되는 새로운 내용이다.")
print("="*20)

# 예시 : len()을 통해서 출력하는 내용과 연동되도록 만든다.
# - 영어에 한해서만 연동이 잘 된다.
word = "Apple Pie is Delicious~~!"
print(len(word)) # 정수값이 나오며 글자수가 나온다.
print(word)
print("_" * len(word))