#Tại vương quốc Valoria, hiệp sĩ Arion được giao nhiệm vụ giải mã những mật thư bí ẩn do kẻ thù gửi đến. Mỗi mật thư là một chuỗi ký tự, và chỉ những mật thư có điểm khởi đầu trùng khớp với điểm kết thúc mới được xem là thông điệp hợp lệ để mở khóa Cổng Ánh Sáng.
#Hiệp sĩ Arion cần bạn giúp anh ta xác định xem từng mật thư có hợp lệ hay không.
#Yêu cầu
#Với mỗi chuỗi ký tự được cung cấp, hãy kiểm tra:
#Nếu ký tự đầu tiên và ký tự cuối cùng của chuỗi giống nhau, in ra "YES".
#Ngược lại, in ra "NO".

#Input
#Dòng đầu tiên là số nguyên t — số lượng mật thư cần kiểm tra.
#Tiếp theo là t dòng, mỗi dòng chứa một chuỗi s (không có khoảng trắng).

#Output
#In ra "YES" nếu chuỗi là mật thư hợp lệ.
#In ra "NO" nếu không hợp lệ.

#Ràng buộc
#1 ≤ t ≤ 100
#1 ≤ |s| ≤ 1000
#Chuỗi s chỉ gồm các ký tự chữ cái hoặc chữ số.


t = int(input())
for _ in range(t):
    s =input()
    if s[0] == s[-1]:
        print("YES")
    else:
        print("NO")