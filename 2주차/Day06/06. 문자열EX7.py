address = "부산시 수영구 수영로 310번길"
# 시작은 생략할 수 있다.
print("시 :",address[:3]) # address[0:3]
print("구 :",address[4:4+3])
print("도로 :",address[-9:]) # address[17-9:17] -> address[8:17]
# 마지막은 생략할 수 있다.

# 응용형태 : 분리할거면, 원본은 필요없다.
address = "부산시 수영구 수영로 310번길"
part1 = address[:3] # 앞부분 복사
address = address[4:] # 앞부분 제외한 뒷부분으로 덮어쓰기
print(part1, address)
address = "수영구 수영로 310번길"
part2 = address[:3] # 앞부분 복사
address = address[4:] # 앞부분 제외한 뒷부분으로 덮어쓰기
print(part1, part2, address)
address = "수영로 310번길"
part3 = address[:] # 전체 복사
address = "" # 원본값 제거
print(part1, part2, part3) # 완벽하게 분리된 3개