lst = []
count = 1
while count <= 5:
    value =  int( input( "%d번 정수 >> "%(count) ) )
    # 메서드 : 특정 객체에서 사용가능한 전용함수
    lst.append( value ) # lst += [ value ]
    # append : 리스트에 값을 추가해주고, 값은 후미에 추가된다.
    count += 1

print(lst)
count = 1
# len( ) : 크기를 구해주는 함수
# 리스트에 대해서는 값의 수량을 구해준다.
# - 리스트를 만들었으면, 리스트의 크기를 기반으로 연동시킨다.
while count <= len(lst):
    print( "뒤에서 %d번 : %d"%(count, lst[-count]) )
    count += 1