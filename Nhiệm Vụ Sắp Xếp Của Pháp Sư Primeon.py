#Tại vùng đất Numeria, pháp sư Primeon được giao nhiệm vụ bảo vệ Thư Viện Số Nguyên Tố – nơi chứa đựng những con số có sức mạnh đặc biệt. Tuy nhiên, một trận bão ma thuật đã khiến các con số trong thư viện bị xáo trộn.
#Primeon cần khôi phục trật tự bằng cách chỉ sắp xếp lại các số nguyên tố, trong khi giữ nguyên vị trí của các số không phải nguyên tố.

#Mô tả nhiệm vụ
#Cho một dãy gồm n số nguyên. Hãy sắp xếp tăng dần các số nguyên tố trong dãy, nhưng không thay đổi vị trí của các số không phải nguyên tố.

#Input
#Dòng đầu chứa số nguyên n — số phần tử của dãy.
#Dòng thứ hai chứa n số nguyên cách nhau bởi khoảng trắng.

#Output
#In ra dãy số sau khi đã sắp xếp lại theo quy tắc trên.

#Ràng buộc
#1 ≤ n ≤ 10^5
#1 ≤ a[i] ≤ 10^6


n = int(input())
danh_sach_so = list(map(int, input().split()))
def la_so_nguyen_to(so):
    if so <= 1: 
        return False
    for i in range(2, int(so**0.5) + 1):
        if so % i == 0:
            return False
    return True
cac_so_nguyen_to = []         
vi_tri_nguyen_to = [] 
for chi_so, so in enumerate(danh_sach_so):
    if la_so_nguyen_to(so):
        cac_so_nguyen_to.append(so)
        vi_tri_nguyen_to.append(chi_so)
cac_so_nguyen_to.sort()
ket_qua = danh_sach_so.copy() 
for i in range(len(vi_tri_nguyen_to)):
    vi_tri_goc = vi_tri_nguyen_to[i]
    so_nguyen_to_da_sap_xep = cac_so_nguyen_to[i]
    ket_qua[vi_tri_goc] = so_nguyen_to_da_sap_xep
print(*(ket_qua))
