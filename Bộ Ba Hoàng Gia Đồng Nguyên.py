#Trong vương quốc Numeria, nhà toán học cổ đại Alaric muốn tìm các bộ ba số nguyên dương từ một khoảng a đến b để tạo ra Bộ Ba Hoàng Gia Đồng Nguyên.
#Một bộ ba (i, j, k) được coi là đồng nguyên nếu mọi cặp số trong bộ đều nguyên tố cùng nhau (gcd = 1).

#Nhiệm vụ
#Nhập hai số nguyên a và b (a ≤ b).
#Tìm tất cả các bộ ba số (i, j, k) sao cho:
#a ≤ i < j < k ≤ b
#gcd(i, j) = gcd(j, k) = gcd(i, k) = 1
#In ra tất cả bộ ba theo định dạng: (i, j, k) mỗi bộ trên một dòng.

#Dữ liệu vào
#Một dòng: hai số nguyên a b

#Dữ liệu ra
#Nhiều dòng, mỗi dòng chứa một bộ ba (i, j, k) thỏa mãn điều kiện.


a,b = map(int,input().split())
import math
for i in range(a,b+1):
    for j in range(i+1,b+1):
        for k in range(j+1,b+1):
            if math.gcd(i,j) == 1 and math.gcd(j,k) == 1 and math.gcd(i,k) == 1:
                print(f"({i},{j},{k})")