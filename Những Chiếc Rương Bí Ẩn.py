#Tại cảng biển Marinthia, thuyền trưởng Selene phát hiện một kho báu cổ xưa chứa đầy những chiếc rương đôi. Mỗi rương được đánh số theo mã hai chữ số, và toàn bộ kho báu được ghi lại dưới dạng một chuỗi số liên tiếp mà không có dấu cách.
#Selene muốn nhanh chóng xác định tất cả các mã rương xuất hiện trong kho và số lượng lần xuất hiện của từng mã, để lập bản đồ kiểm kê kho báu.

#Nhiệm vụ
#Nhập vào một chuỗi số a, có độ dài chẵn.
#Chia chuỗi thành các đoạn 2 chữ số liên tiếp.
#Đếm số lần xuất hiện của từng đoạn.
#In ra tất cả các mã rương (hai chữ số) mà xuất hiện, theo không cần thứ tự.

#Dữ liệu vào
#Một dòng: chuỗi số a (độ dài chẵn, chỉ gồm chữ số 0–9).

#Dữ liệu ra
#In ra các số nguyên (mã rương) xuất hiện trong chuỗi, cách nhau một khoảng trắng.

#Ràng buộc
#Độ dài chuỗi a chẵn và 2 ≤ |a| ≤ 10^6
#Chuỗi chỉ gồm các ký tự '0'–'9'


string = input()
lst = []
start = 0
while start < len(string):
    lst.append(string[start : start + 2])
    start += 2
ans = []
for index, nums in enumerate(lst):
    if nums not in ans:
        ans.append(nums)
print(*ans)