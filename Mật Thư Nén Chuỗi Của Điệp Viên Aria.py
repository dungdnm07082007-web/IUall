#Trong tổ chức mật vụ Eclipse, điệp viên Aria chuyên phụ trách giải mã và mã hóa thông tin tuyệt mật. Để tiết kiệm dung lượng và tránh bị phát hiện, cô thường sử dụng một kỹ thuật đặc biệt gọi là nén chuỗi liên tiếp.
#Một thông điệp được viết dưới dạng chuỗi ký tự, trong đó các ký tự liên tiếp giống nhau sẽ được thay thế bằng số lượng lặp lại theo sau là ký tự đó. Nhiệm vụ của bạn là giúp Aria tự động hóa quá trình này.

#Input
#Dòng đầu tiên chứa số nguyên t — số lượng thông điệp cần mã hóa.
#Mỗi trong t dòng tiếp theo chứa một chuỗi ký tự s.

#Output
#Với mỗi chuỗi s, in ra chuỗi đã được nén theo quy tắc:
#Với mỗi dãy ký tự liên tiếp giống nhau, in ra <số lượng><ký tự>.
#Các phần được in nối liền nhau thành một chuỗi duy nhất.

#Ràng buộc
#1 ≤ t ≤ 100
#1 ≤ |s| ≤ 1000
#Chuỗi s chỉ gồm các ký tự chữ cái in hoa (A–Z).


t = int(input())
for _ in range(t):
    s = input()
    result = ""
    so_luong = 1
    ky_tu = s[0]
    for i in range(1, len(s)):
        if s[i] == ky_tu:
            so_luong += 1
        else:
            result += str(so_luong) + ky_tu
            ky_tu = s[i]
            so_luong = 1
    result += str(so_luong) + ky_tu
    print(result)