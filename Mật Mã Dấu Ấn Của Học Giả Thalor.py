#Tại thư viện cổ Aetherium, học giả Thalor đang nghiên cứu một bản văn bị phong ấn bằng Mật Mã Dấu Ấn. Bản văn này gồm các ký tự dấu ngoặc tròn "(" và ")". Mỗi cặp ngoặc tượng trưng cho một dấu ấn phép thuật – khi một dấu ấn mở ra, nó được gán một mã số duy nhất; khi đóng lại, nó phải khớp với mã số của dấu ấn đã mở trước đó.
#Thalor cần bạn giúp ông xác định mã số tương ứng với từng dấu ngoặc trong bản văn, để khôi phục trình tự phép thuật ẩn bên trong.

#Nhiệm vụ của bạn là:
#Với mỗi chuỗi dấu ngoặc, đánh số thứ tự cho các dấu mở "(" từ 1 trở đi theo thứ tự xuất hiện.
#Khi gặp dấu đóng ")", in ra số hiệu của dấu mở tương ứng gần nhất.

#Input
#Dòng đầu tiên chứa số nguyên t — số lượng bản văn cần giải mã.
#Tiếp theo là t dòng, mỗi dòng là một chuỗi gồm các ký tự "(" và ")".

#Output
#Với mỗi bản văn, in ra dãy số tương ứng với từng dấu ngoặc theo thứ tự xuất hiện, cách nhau bằng khoảng trắng.


t = int(input())
while t > 0:
    string = input().strip()
    lst = []
    cnt = 0
    for ch in string:
        if ch == "(":
            cnt += 1
            lst.append(cnt)
            print(lst[len(lst) - 1], end = " ")
        else:
            print(lst[len(lst) - 1], end = " ")
            lst.pop(len(lst) - 1)    
    print()
    t -= 1
