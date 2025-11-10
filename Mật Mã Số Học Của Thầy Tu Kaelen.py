#Trong tu viện cổ Numis, thầy tu Kaelen đang nghiên cứu một loại mật mã số học được khắc trên những tấm bia đá. Mỗi tấm bia chứa một chuỗi ký tự số, được cho là ẩn chứa hai năng lượng: năng lượng chẵn và năng lượng lẻ.
#Theo truyền thuyết, các chữ số ở vị trí lẻ (đếm từ 1) sinh ra năng lượng nhân, còn các chữ số ở vị trí chẵn sinh ra năng lượng cộng.
#Nhiệm vụ của bạn là giúp Kaelen tính toán hai giá trị này cho mỗi chuỗi số:
#Tích của tất cả các chữ số ở vị trí lẻ khác 0.
#Tổng của tất cả các chữ số ở vị trí chẵn.
#Nếu không có chữ số nào khác 0 ở vị trí lẻ, coi tích bằng 0.

#Input
#Dòng đầu tiên chứa số nguyên t — số lượng chuỗi số được khắc trên bia đá.
#Tiếp theo là t dòng, mỗi dòng chứa một chuỗi ký tự số s.

#Output
#Với mỗi chuỗi, in ra hai số nguyên cách nhau một khoảng trắng:
#Số thứ nhất là tích các chữ số ở vị trí lẻ (không tính số 0).
#Số thứ hai là tổng các chữ số ở vị trí chẵn.


t = int(input())
for _ in range(t):
    s = input().strip()
    tong = 0
    tich = 1
    le = False
    for i in range(len(s)):
        so = int(s[i])
        if (i +1) % 2 == 1:
            if so != 0:
                tich *= so
                le = True
        else:
            tong += so
        if not le:
            tich = 0
    print(tich, tong)