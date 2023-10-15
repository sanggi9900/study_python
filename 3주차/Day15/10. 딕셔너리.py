# 딕셔너리 : 중복을 허용하지 않는 자료구조
# - 값들은 "키"에 의하여 구분되고 관리되기 때문이다.
lst1 = []
lst2 = ["홍길동",23,99.8]
info1 = {}
info2 = {"name":"홍길동", "age":23, "score":99.8 }
# - 사용할 때는 키를 직접 지정해서 이용한다.
print(lst2[0], lst2[1])
print(info2["name"],info2["age"])

# - 딕셔너리는 리스트처럼 값들을 한번에 관리해주는 컨테이너같은 개념
print(lst2)
print(info2)

# - 리스트처럼 연산기능이 없다.
lst1 += [10] # lst1.append(10) # 리스트의 연산기반 동작
info1["value1"] = 10 # 변수를 생성하고 저장하는 동작
print(lst1, info1)

# - 리스트처럼 슬라이싱이 안된다.
name_from_lst = lst2[0]
lst2.pop(0) # lst2[0:1] = [] # 지정인덱스의 값 제거
print(name_from_lst, lst2)
name_form_dic = info2["name"]
info2.pop("name") # 지정한 키 및 값 제거. 딕셔너리는 메서드에 의해서만 제거 가능 
print(name_form_dic, info2)