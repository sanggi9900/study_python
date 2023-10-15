lst1 = [1,2,3]
lst2 = [4,5,6]
lst3 = []
lst4 = lst1 + lst2
print("합친 리스트 :",lst4)
# 슬라이싱 잘 활용해서 달성합니다.
# - 참고 : 리스트는 최대한 적게 만들어져야 함
# - 리스트는 대괄호 열어서 만드는 순간, 새롭게 만들어진다.
# - 변수에 저장하지 않더라도 매번 생성되니 주의할 것.
lst4[2:4] = lst3
print("1단계 :", lst4)
lst4[1:1] = lst1
print("2단계 :", lst4)
lst4[-1:-1] = lst2
print("3단계 :", lst4)
lst4 = lst4[4:6]
print("4단계 :", lst4)
lst4[1:1] = lst1 + lst2
print("5단계 :", lst4)