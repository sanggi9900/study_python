# ((반복하기) + 합치기) * 반복하기
size = int(input("출력할 크기 입력 >> "))
# 3일 경우
print(("ㅁ" * size + '\n') * size, end="")
# 팁 : 마지막은 불필요하지만 이런 것을 할 때는 붙여서 보는게 좋습니다.

# 추가팁 : print에는 옵션이 존재한다.
# end, sep를 잘 활용하면 좋다.
# 1) end : print의 줄바꿈을 바꿔준다.
print("Apple", end="") # end='\n'
print("Pie", end = "~~~")
print("Delicious")

# 2) sep : 쉼표에 의한 띄어쓰기를 바꿔준다.
print(123,456,789)
print(123,456,789, sep="") # sep = ' '
print(123,456,789, sep='\n')

# 3) 둘은 같이 쓸 수 있음. 순서 상관없이 마지막에만 붙이면 된다.
print(123,456,sep="WOW", end="END~!\n")