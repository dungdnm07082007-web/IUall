#Trong một vương quốc số học, hiệp sĩ Divisor sở hữu một tập hợp các viên đá thần, mỗi viên được khắc một số nguyên. Hiệp sĩ muốn tìm tất cả các cặp đá "đồng hành", nghĩa là hai viên đá không có ước chung ngoài 1 (gcd = 1).
#Nhiệm vụ của bạn là giúp hiệp sĩ liệt kê tất cả các cặp đồng hành từ tập hợp đá.

#Input
#Dòng đầu tiên chứa một số nguyên n — số lượng viên đá.
#Dòng thứ hai chứa n số nguyên a[i] — giá trị trên mỗi viên đá.

#Output
#In ra tất cả các cặp số (a[i], a[j]) thỏa mãn:
#i < j
#gcd(a[i], a[j]) = 1
#Mỗi cặp in trên một dòng, theo thứ tự i tăng dần, nếu i bằng nhau thì theo j tăng dần.


def gcd(a, b):
    while(b != 0):
        tmp = a % b
        a = b
        b = tmp
    return a
n = int(input())
lst = list(map(int, input().split()))
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if gcd(lst[i], lst[j]) == 1:
            print(lst[i], lst[j], end = "\n")