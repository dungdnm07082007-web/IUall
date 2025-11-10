#Trong tháp pha lê của Eldoria, pháp sư Eldrin đang thực hiện một nghi thức cổ xưa có tên là “Hoán Vị Trật Tự”. Nghi thức này nhằm mở ra Cổng Ánh Sáng — nơi chỉ những chuỗi số được sắp xếp theo mọi cách có thể mới đủ năng lượng kích hoạt.
#Để hoàn thành nghi thức, Eldrin cần:
#Xác định tổng số hoán vị khả dĩ của các con số từ 1 đến n.
#Liệt kê toàn bộ các hoán vị đó theo thứ tự giảm dần từng vị trí.
#Bạn được giao nhiệm vụ hỗ trợ Eldrin hoàn thành phép triệu hồi này.

#Input
#Dòng đầu tiên chứa số nguyên t — số lượng nghi thức cần thực hiện.
#Với mỗi nghi thức:
#Một dòng chứa số nguyên n — số lượng con số tham gia nghi thức.

#Output
#Dòng đầu tiên in ra tổng số hoán vị có thể tạo ra từ 1 đến n.
#Dòng tiếp theo in ra toàn bộ các hoán vị, mỗi hoán vị là một chuỗi liền nhau các chữ số, cách nhau bởi một khoảng trắng.

#Ràng buộc
#1 ≤ t ≤ 5
#1 ≤ n ≤ 8


DU_LIEU_DAU_VAO = ""
def tinh_gt(n):
    gt = 1
    for i in range(1, n + 1):
        gt *= i
tat_ca = DU_LIEU_DAU_VAO.strip().split('\n')    
T = int(tat_ca[0].strip())
dong_hien_tai = 1   
for _ in range(T):
    N = int(tat_ca[dong_hien_tai].strip())
    dong_hien_tai += 1
    tong_hv = tinh_gt(N)
    print(tong_hv)
    cac_so = list(range(1, N + 1))
    ds_hv = []    
    def tao_hv(so_con_lai, hv_hien_tai):
        if not so_con_lai:
            ds_hv.append(list(hv_hien_tai))
            return
        for i in range(len(so_con_lai)):
            so_chon = so_con_lai[i]
            so_tiep_theo = so_con_lai[:i] + so_con_lai[i+1:]
            tao_hv(so_tiep_theo, hv_hien_tai + [so_chon])
    tao_hv(cac_so, [])
    ds_hv.reverse()
    for hv in ds_hv:
        chuoi_hv = ' '.join(map(str, hv))
        print(chuoi_hv)