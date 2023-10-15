def make_sum_from(lst):
    result = 0
    for value in lst:
        result += value
    return result
def make_sum_with(n1, n2):
    if n1 == n2:
        return n1
    else:
        result = 0
        if n1 < n2:
            values = range(n1,n2+1)
        else:
            values = range(n2,n1+1)
        for value in values:
            result += value
        return result
def make_sum(num):
    if num <= 0:
        return 0
    else:
        result = 0
        for i in range(1, num + 1):
            result += i
        result *= 5
        return result
print("결과1 :", make_sum_from( [1,4,7,10,13] ))
print("결과2-1 :", make_sum_with(3,6))
print("결과2-2 :", make_sum_with(6,3))
print("결과3 :", make_sum(4))