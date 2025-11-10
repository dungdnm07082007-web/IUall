#Bài toán
#Kiểm tra xem số nguyên sau khi đảo ngược 2 lần có giữ nguyên giá trị không.

#Input: số nguyên num
#Output: true nếu giữ nguyên
#Ràng buộc: 0 <= num <= 10^6


import sys
num = input()
if not num:
    sys.exit()
num = int(num)
if num == 0 or num % 10 != 0:
    print("true")
else:
    print("false")