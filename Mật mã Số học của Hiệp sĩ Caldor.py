#Trong vương quốc Numera, có một vị hiệp sĩ tên Caldor — người canh giữ những cuộn mật mã số học cổ đại. Mỗi chuỗi số được khắc trên đá có thể là “Mật mã hợp lệ” hoặc “Vô nghĩa”, và chỉ khi giải mã đúng, cánh cổng Kho Báu Số Học mới mở ra.
#Caldor giao cho bạn nhiệm vụ: kiểm tra từng chuỗi số để xác định xem đó có phải là mật mã hợp lệ hay không.
#Một chuỗi số được xem là mật mã hợp lệ khi:
#Tổng các chữ số chia hết cho 10.
#Hiệu giữa hai chữ số liên tiếp trong chuỗi luôn bằng 2 (tuyệt đối).

#Input
#Dòng đầu chứa số nguyên t — số lượng chuỗi cần kiểm tra.
#t dòng tiếp theo, mỗi dòng chứa một chuỗi số s.

#Output
#Với mỗi chuỗi, in ra:
#"YES" nếu chuỗi là mật mã hợp lệ.
#"NO" nếu không hợp lệ.

#Ràng buộc
#1 ≤ t ≤ 1000
#Mỗi chuỗi s chỉ gồm chữ số (0–9), độ dài không quá 18.


import sys
du_lieu_nhap = sys.stdin.read().split()
so_luong_chuoi_t = int(du_lieu_nhap[0])
chi_so_bat_dau = 1
for i in range(so_luong_chuoi_t):
    chuoi_s = du_lieu_nhap[chi_so_bat_dau + i]
    day_so = [int(ky_tu) for ky_tu in chuoi_s]
    la_mat_ma_hop_le = True 
    tong_cac_chu_so = sum(day_so)
    if tong_cac_chu_so % 10 != 0:
        la_mat_ma_hop_le = False
    if la_mat_ma_hop_le and len(day_so) >= 2:
        for j in range(len(day_so) - 1):
            so_thu_nhat = day_so[j]
            so_thu_hai = day_so[j+1]
            hieu_tuyet_doi = abs(so_thu_nhat - so_thu_hai)
            if hieu_tuyet_doi != 2:
                la_mat_ma_hop_le = False
                break                  
    if la_mat_ma_hop_le:
        print("YES")
    else:
        print("NO")