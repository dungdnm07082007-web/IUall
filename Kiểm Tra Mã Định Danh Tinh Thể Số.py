#Thị Trấn Mạng Lưới – Kiểm Tra Địa Chỉ Tinh Thể Số
#Bối cảnh
#Tại Thị Trấn Mạng Lưới Arbitra, mọi công dân phải sở hữu một Mã Định Danh Tinh Thể Số để có thể kết nối vào Hệ Thống Liên Kết Trung Tâm. Mỗi mã định danh được biểu diễn dưới dạng 4 cụm số, ngăn cách bởi dấu chấm ".".
#Người chịu trách nhiệm kiểm tra và xác thực mã là Iris, một nữ học giả thông thạo ngôn ngữ số học. Nhiệm vụ của Iris là xác định xem một mã định danh có hợp lệ hay không theo luật của hội đồng:
#Mã phải được chia thành đúng 4 phần.
#Mỗi phần chỉ được chứa ký tự số.
#Giá trị số của từng phần phải nằm trong khoảng từ 0 đến 255.
#Nếu mã hợp lệ, Iris sẽ cho phép công dân “Kết nối”, ngược lại sẽ phải từ chối.

#Yêu cầu
#Với mỗi công dân, bạn được cung cấp một chuỗi biểu diễn mã định danh. Hãy xác định xem mã có hợp lệ hay không.
#Hợp lệ → in "YES"
#Không hợp lệ → in "NO"

#Input
#Dòng đầu: số nguyên t – số lượng công dân.
#Mỗi dòng tiếp theo là một chuỗi biểu diễn mã định danh dạng x1.x2.x3.x4.

#Output
#Với mỗi công dân, in "YES" hoặc "NO" tương ứng với tính hợp lệ của mã.


t = int(input())
while t > 0:
    string = input().strip()
    lst = string.split(".")
    check = True
    size = 0
    for ch in lst:
        if ch.isdigit():
            size += 1
            if len(ch) > 1 and ch[0] == "0":
                check = False
            if not (0 <= int(ch) <= 255):
                check = False
        else:
            check = False
    if size != 4:
        check = False
    print("YES" if check else "NO")
    t -= 1