#Câu chuyện:
#Cô Mai, giáo viên toán của trường Nam Dương, muốn hiển thị các số lớn dưới dạng dễ đọc hơn. Cô yêu cầu bạn chèn dấu phẩy vào chuỗi số, tính từ phải sang trái, mỗi ba chữ số một nhóm.

#Nhiệm vụ
#Cho một chuỗi số s, chèn dấu phẩy , từ phải sang trái, sau mỗi 3 chữ số liên tiếp, và in ra kết quả.

#Input
#Một dòng duy nhất chứa chuỗi s gồm các chữ số (1 ≤ |s| ≤ 1000)

#Output
#In ra chuỗi mới sau khi chèn dấu phẩy, không có dấu phẩy thừa ở đầu hoặc cuối


def dequy(s):
    if len(s) <= 3:
        return s
    return dequy(s[:-3]) + ',' + s[-3:]
s = input()
print(dequy(s))