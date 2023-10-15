# 이스케이프는 많이 써봐야 연습이 되고
# 이스케이프는 단독으로 쓰는 일은 \n, \t 빼고는 거의 없습니다.
# 팁 : 필요하니까 쓰는거고, 없다해서 문제가 생기지 않는다.
# -> 나중에 추가해도 별 문제가 없다.

print("QUICK Brown Fox JUMP over the LAZY DOG") # 원본
print("QUICK Brown Fox\nJUMP over\nthe LAZY DOG") # 줄바꿈 추가
print("\"QUICK\" Brown \"Fox\"\nJUMP over\nthe LAZY DOG") # 따옴표 추가
print("\"QUICK\" Brown \"Fox\"\nJUMP 'over'\nthe LAZY DOG") # 따옴표 추가
print("\"QUICK\" Brown \"Fox\"\nJUMP 'over'\n\"the LAZY DOG\"") # 완성본
print('"QUICK" Brown "Fox"',"\nJUMP 'over'",'\n"the LAZY DOG"') # 교차시킨 경우

# 1. 큰 따옴표 내에서 큰 따옴표는 절대 쓸 수 없음
# 2. 작은 따옴표 내에서 작은 따옴표는 절대 쓸 수 없음
# 3. 교차는 가능하지만, 교차하면 코드가 복잡해짐
# 4. 일관성있는 코드를 작성하기 위한 것