#Pháp sư Arthel là người trông giữ Tháp Ký Ức, nơi chứa hàng ngàn cuộn mật thư cổ. Mỗi cuộn thư được mã hóa bằng một chuỗi ký tự số. Tuy nhiên, chỉ những cuộn thư có dãy số tăng dần hoặc giữ nguyên theo thứ tự từ trái sang phải mới được xem là “ổn định” và có thể mở khóa.
#Arthel muốn kiểm tra một loạt mật mã để xác định xem chúng có phải là chuỗi ổn định hay không. Nhiệm vụ của bạn là giúp ông ta.
#Một chuỗi được coi là ổn định nếu với mọi vị trí i, ký tự ở vị trí i không lớn hơn ký tự ở vị trí i+1.

#Input
#Dòng đầu chứa số nguyên t — số lượng mật mã cần kiểm tra.
#Mỗi trong t dòng tiếp theo chứa một chuỗi ký tự số s.

#Output
#Với mỗi chuỗi, in ra:
#"YES" nếu chuỗi là ổn định.
#"NO" nếu chuỗi không ổn định.

#Ràng buộc
#1 ≤ t ≤ 100
#1 ≤ |s| ≤ 1000
#s chỉ bao gồm các chữ số '0'–'9'


t = int(input())
while t > 0:
    str = input().strip()
    check = True
    for i in range(1, len(str)):
        if int(str[i]) < int(str[i - 1]):
            check = False
    if check:
        print("YES")
    else:
        print("NO")
    t -= 1