#Bài toán
#Xét một thuật toán nhận vào một số nguyên dương n.
#Nếu n chẵn, thuật toán chia n cho 2.
#Nếu n lẻ, thuật toán nhân n với 3 và cộng 1.
#Thuật toán lặp lại cho đến khi n bằng 1.

#Input
#Một dòng duy nhất chứa số nguyên n.

#Output
#In ra một dòng chứa tất cả các giá trị của n trong quá trình thuật toán.

#Constraints
#1 ≤ n ≤ 10^6


lst = []
n = int(input())
while n != 1:
    lst.append(n)
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n +1
lst.append(1)
print(" ".join(map(str,lst)))