# ★★★ 딕셔너리 그자체를 while로는 못돌리니 주의
lst = ["이름","나이","취미","꿈"]
# 목록 준비할 때 주의사항 : 문자열은 변수생성규칙대로 만드셔야 한다.
dic1 = {}
# 반복을 돌릴려면 반드시 숫자놀음이 되어야 한다.
index = 0
while index < len(lst):
    dic1[lst[ index ]] = input( lst[ index ] + " 입력 >> " )
    index += 1

index = 0
while index < len(lst):
    print("%s\t: %s"%( lst[ index ], dic1[ lst[ index ] ] ) )
    index += 1