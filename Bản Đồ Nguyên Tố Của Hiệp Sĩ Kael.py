#Tại vương quốc Ardonia, hiệp sĩ Kael được giao trọng trách khám phá Bản Đồ Số Bí Ẩn – một ma trận cổ đại được khắc trên tấm bia đá trong đền thờ của các nhà tiên tri. Người ta tin rằng chỉ những ô mang năng lượng nguyên tố mới dẫn đường đến kho báu của các bậc tiền nhân.
#Bản đồ được biểu diễn dưới dạng một ma trận kích thước n × m, trong đó mỗi ô chứa một số nguyên dương. Hiệp sĩ Kael cần xác định ô nào chứa sức mạnh nguyên tố (tức là số nguyên tố) và ô nào không.
#Hãy giúp Kael tạo ra bản đồ năng lượng, trong đó:
#Ô chứa số nguyên tố được đánh dấu bằng 1.
#Ô không phải số nguyên tố được đánh dấu bằng 0.

#Input
#Dòng đầu tiên chứa hai số nguyên n, m — số hàng và số cột của ma trận.
#Tiếp theo là n dòng, mỗi dòng chứa m số nguyên.

#Output: In ra ma trận gồm n hàng và m cột, trong đó mỗi phần tử là 1 hoặc 0 tương ứng với việc ô đó có chứa số nguyên tố hay không.


import sys
import math
def is_prime(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0    
    limit = int(math.sqrt(n))    
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return 0            
    return 1
def solve():
    line = sys.stdin.readline().strip().split()
    N = int(line[0])
    M = int(line[1])
    res_mat = []
    for r in range(N):
        data_row = list(map(int, sys.stdin.readline().strip().split()))            
        res_row = []        
        for num in data_row:
            res = is_prime(num)
            res_row.append(str(res))        
        res_mat.append(res_row)
    for row in res_mat:
        print(" ".join(row))
if __name__ == "__main__":
    solve()