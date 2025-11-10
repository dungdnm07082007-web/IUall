#Tại vương quốc Numeria, pháp sư Numerion đang luyện tập một phép thuật liên quan đến các bội số.
#Phép thuật này giúp tìm ra các số bội của k nằm trong khoảng từ a đến n, đồng thời tính hiệu số so với a.
#Bạn, học trò pháp sư Lyra, được giao nhiệm vụ liệt kê các hiệu số này.

#Nhiệm Vụ
#Cho ba số nguyên a, k, n:
#Tìm tất cả số nguyên x thỏa mãn:
#x ≥ a
#x ≤ n
#x chia hết cho k
#Với mỗi số x tìm được, in ra x - a theo thứ tự tăng dần.
#Nếu không có số nào thỏa mãn, in -1.

#Input
#Một dòng: ba số nguyên a, k, n (1 ≤ a, k, n ≤ 10^9)

#Output
#Một dòng: các số x - a cách nhau bằng một khoảng trắng, hoặc -1 nếu không có số nào.

#Ràng buộc
#1 ≤ a, k, n ≤ 10^9


a,k,b = map(int,input().split())
start = (a // k + 1) * k
if start > b:
    print(-1)
else:
    res = [str(x-a)for x in range(start,b+1,k)]
    print(" ".join(res))