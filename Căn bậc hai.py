#Mô tả:
#Tính căn bậc hai nguyên của số nguyên không âm x, làm tròn xuống (floor).

#Input
#x — số nguyên

#Ràng buộc:
#0 <= x <= 2^31 − 1

#Output
#Căn bậc hai nguyên của x (làm tròn xuống).


import sys
import math
x_str = sys.stdin.readline().strip()
if x_str:
    x = int(x_str)
    ket_qua = int(math.sqrt(x)) 
    print(ket_qua)