num = 0
while num <= 0:
    num = int(input("약수를 구할려는 약수 입력 >> "))
# 수학"논리" 를 키우고 싶다면
# - 유튜브 등의 교양영상같은 것이 큰 도움이 됩니다.
print("%d의 약수들"%(num))
for i in range(1,num + 1):
    if num % i == 0:
        if num != i:
            print(i, end=", ")
        else:
            print(i)

# 약수를 구하는 다른 방식 - 규칙성은 없지만 특징은 있다.
print("%d의 약수들"%(num))
for i in range(1,num//2 + 1):
    if num % i == 0:
        print(i, end=", ")
print(num)