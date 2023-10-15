# 유한 + 유한 : 자주 사용하는 조합
# -> x / y 의 조합으로 생각하자 -> 2차원의 평면좌표
for y in range(5): # y축단위 이동(한줄)
    for x in range(7): # y축내에서의 이동(줄 내부의 문자)
        # 단순 출력의 경우
        print("(%d, %d) "%(y, x), end = ' ')
    print()
# -> 2차원 평면을 자료구조를 통해 만들 수 있다.
lst2d = [
#  X  0  1  2  3  4  # Y
    [ 0, 1, 2, 3, 4],# 0
    [ 5, 6, 7, 8, 9],# 1
    [10,11,12,13,14] # 2
]
# 단순하게 사용'만'한다.
for lst1d in lst2d: # 리스트 내부의 리스트를 가져온다.
    print(lst1d)
    for value in lst1d: # 내부의 리스트에 있는 값을 가져온다.
        print("%3d"%(value), end = ' ')
    print()
# 인덱싱을 통해서 굴려먹는다 - 제일 많이 쓰는 방식
print(lst2d[0], lst2d[0][2]) # 인덱싱을 한번 더 하면 값의 사용이 가능하다.
for y in range( len(lst2d) ): # len은 대상이 가진 값의 수량만 세어준다.
    # print(lst2d[y])
    for x in range( len(lst2d[y]) ):
        print(lst2d[y][x], end=' ')
print()

# 번외 : 반복문의 순서를 바꿔주면, 방향을 90도 꺽을 수 있다
for x in range( len(lst2d[0]) ): # len은 대상이 가진 값의 수량만 세어준다.
    # print(lst2d[y])
    for y in range( len(lst2d) ):
        print(lst2d[y][x], end=' ')
print()