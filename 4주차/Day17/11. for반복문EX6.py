lst = []
count = int( input("입력횟수 >> ")[:-1] )
for num in range(1, count + 1):
    value = float( input( "%d번째 실수 >> "%(num) ) )
    lst.append(value)

result = 0
for value in lst:
    result += value

print("목록")
for value in lst:
    print( "%.2f"%(value), end = ' ' )
print( "\n합 : %.2f"%(result) )