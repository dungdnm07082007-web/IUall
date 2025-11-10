#Cho một địa chỉ IP hợp lệ (IPv4), hãy trả về phiên bản "defanged" của địa chỉ IP đó.
#Một địa chỉ IP "defanged" được tạo bằng cách thay thế mọi dấu chấm "." trong địa chỉ IP bằng chuỗi "[.]".


n = input()
print(n.replace('.', '[.]'))