#Cho một dãy gồm N số nguyên dương được đánh số từ 0. Bạn hãy tính tổng các số ở vị trí lẻ của dãy.

#Dữ liệu
# Dòng đầu tiên gồm số nguyên N.
#Dòng thứ hai gồm N số nguyên dương.

#Kết quả
# In ra một số nguyên duy nhất là kết quả bài toán.

#Giới hạn
# 0 ≤ N ≤ 105
# Các số có giá trị tuyệt đối không quá 10^9


so_luong_phan_tu = int(input())
so_luong_phan_tu = 0 
day_so = list(map(int, input().split()))
day_so = []
tong_cac_so_vi_tri_le = sum(day_so[1::2])
print(tong_cac_so_vi_tri_le)

