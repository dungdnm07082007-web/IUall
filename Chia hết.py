#Kiểm tra xem số nguyên dương n có chia hết đồng thời cho 2, 3 và 5 hay không.

#Input: một số nguyên dương n
#Output: boolean (true nếu chia hết cho cả 3 số, false nếu không)


n = int(input())
if n % 2 == 0 and n % 3 == 0 and n % 5  == 0:
    print("true")
else:
    print("false")