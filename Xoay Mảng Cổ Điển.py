#Tại Làng Thuật Toán, các học sinh được giao một nhiệm vụ xoay mảng theo số bước cố định.
#Nhân vật chính: bạn, một học sinh ham mê thuật toán.

#Nhiệm vụ: cho một mảng các số nguyên, xoay mảng sang trái k bước.
#Mỗi bước xoay sẽ di chuyển phần tử đầu tiên của mảng lên cuối cùng.

#Mô tả nhiệm vụ
#Bạn nhận được một mảng gồm n số nguyên.
#Bạn được yêu cầu xoay mảng sang trái k bước.
#In mảng sau khi xoay.

#Input
#Dòng 1: số nguyên t – số lượng test case (1 ≤ t ≤ 100)
#Mỗi test case gồm 2 dòng:
#Dòng 1: hai số nguyên n k – độ dài mảng và số bước xoay (1 ≤ k ≤ n ≤ 10^5)
#Dòng 2: n số nguyên – các phần tử của mảng

#Output
#Với mỗi test case, in mảng sau khi xoay sang trái k bước, các phần tử cách nhau bởi khoảng trắng


t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    k = k % n
    result = a[k:] + a[:k]
    print(" ".join(map(str, result)))