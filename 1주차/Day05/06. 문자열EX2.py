fnum = 3.141516171819
word = "ABCDEFG"
num = 456789
print("%.6f"%(fnum))
print("%.4f"%(fnum))
print("%.2f"%(fnum))
print("%.2s %.3s %.4s"%(word, word, word))
print("%.4d%.5d%.6d"%(num, num, num)) # 각 개별값에 대한 서식을 적용
print("0%d00%d000%d"%(num, num, num)) # 전체 출력형태에 대한 서식을 적용