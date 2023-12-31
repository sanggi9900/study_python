ram = 16
print("Ram 16짜리인가?", ram == 16)
print("Ram 32짜리인가?", ram == 32)
# 논리합(or)
# - 조건식들 중 적어도 하나를 만족하는 경우의 수를 찾는다.
# - 조건식들이 모두 부정되는 경우의 수를 찾을 수 있다.
print("Ram이 16 또는 32짜리인가?", ram == 16 or ram == 32)

# 논리곱(and)
# - 조건식들을 모두 만족하는 유일한 것을 찾는다.
display = 16
# 정확하게 16인치 이상, 17인치 미만만 찾는다.
result = display >= 16 and display < 17
print("화면이 16인치대인가?", result)
# 16인치대이면서 램이 16인 것만 정확하게 찾는다.
print("RAM이 16이면서 16인치대인가?", ram == 16 and result)

# 부정(not)
# - 긍부부/부부긍 용도이지만, 꼼수용으로 쓰기도 한다.
# - 사람은 보고 싶은건 엄청 잘 보이고, 잘 찾지만...
print("화면이 16인치대가 아닌가?", not result)
# - 그 외의 것은 잘 안보인다.
print("RAM이 16이 아니면서 16인치대아닌 것인가?", not (ram == 16 and result))