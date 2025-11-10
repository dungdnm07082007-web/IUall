#Tại Học viện Magica, thầy hiệu trưởng đang muốn quản lý thông tin thí sinh tham gia kỳ thi tuyển sinh phép thuật.
#Mỗi thí sinh có họ tên, ngày sinh, điểm 3 môn thi.
#Bạn, trợ lý pháp sư Lyra, được giao nhiệm vụ tính tổng điểm và in thông tin thí sinh.

#Nhiệm Vụ
#Nhập thông tin một thí sinh:
#Họ tên
#Ngày sinh (dd/mm/yyyy)
#Điểm môn 1, môn 2, môn 3
#Tính tổng điểm 3 môn.
#In ra thông tin thí sinh theo định dạng:
#Họ_Tên Ngày_Sinh Tổng_Điểm
#Tổng điểm in 1 chữ số thập phân.

#Input
#Dòng 1: Họ tên thí sinh (chuỗi, độ dài ≤ 100)
#Dòng 2: Ngày sinh (chuỗi, định dạng dd/mm/yyyy)
#Dòng 3: Điểm môn 1 (thực)
#Dòng 4: Điểm môn 2 (thực)
#Dòng 5: Điểm môn 3 (thực)

#Output
#Một dòng in thông tin thí sinh:
#Họ_Tên Ngày_Sinh Tổng_Điểm


ho_ten = input()
ngay_sinh = input()
diem_m1 = float(input())
diem_m2 = float(input())
diem_m3 = float(input())
tong_diem = diem_m1 + diem_m2 + diem_m3
print(f"{ho_ten} {ngay_sinh} {tong_diem:.1f}")