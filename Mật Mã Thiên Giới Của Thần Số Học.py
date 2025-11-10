#Trong vương quốc Numenra, tồn tại một tộc cổ xưa gọi là Thần Số Học, họ tin rằng chỉ những con số chứa sức mạnh thuần khiết mới có thể mở cánh cổng dẫn đến vùng đất thiêng Elarion.
#Người gác cổng, Thầy cả Arven, trao cho bạn nhiệm vụ kiểm tra một loạt mật mã. Mỗi mật mã là một chuỗi ký tự chỉ gồm các chữ số. Arven cho biết chỉ những mật mã hoàn toàn được tạo nên từ các chữ số 4 và 7 mới được xem là “Mật Mã Thiên Giới”.
#Hãy giúp Arven xác định xem từng mật mã có đạt chuẩn hay không.

#Input
#Dòng đầu chứa số nguyên t — số lượng mật mã cần kiểm tra.
#Mỗi dòng tiếp theo chứa một chuỗi s — mật mã.

#Output
#Với mỗi mật mã, in ra YES nếu đó là Mật Mã Thiên Giới, ngược lại in ra NO.

#Ràng buộc
#1 ≤ t ≤ 100
#1 ≤ |s| ≤ 100
#Mỗi ký tự trong s là chữ số '0'–'9'


t = int(input())
for _ in range(t):
    s = input()
    is_valid = True
    for ch in s:
        if ch != '4' and ch != '7':
            is_valid = False
            break
    print("YES" if is_valid else "NO")