#Tại xưởng vẽ cổ Eldoria, họa sư Lirien đang chuẩn bị cho buổi triển lãm tranh hình học. Mỗi bức tranh của bà được tạo từ một hình chữ nhật ma thuật, trong đó chiều rộng, chiều cao và màu sắc đều mang ý nghĩa đặc biệt.
#Tuy nhiên, không phải hình nào cũng hợp lệ — nếu chiều rộng hoặc chiều cao không dương, bức tranh sẽ biến mất khỏi khung tranh. Lirien cần bạn giúp kiểm tra tính hợp lệ của hình và hiển thị thông tin của nó.

#Nhiệm vụ
#Với ba giá trị: chiều rộng w, chiều cao h và màu sắc color của một hình chữ nhật, hãy xác định xem hình đó có hợp lệ không.
#Nếu hợp lệ, in ra chu vi, diện tích và màu sắc (màu được chuẩn hóa: chữ cái đầu viết hoa, còn lại viết thường).
#Nếu không hợp lệ, in ra "INVALID".

#Input
#Gồm một dòng chứa ba giá trị: w h color
#w, h: hai số nguyên biểu thị chiều rộng và chiều cao.
#color: chuỗi ký tự không có dấu cách.

#Output
#Nếu hình hợp lệ: in ra chu vi, diện tích, tên màu chuẩn hóa.
#Nếu không hợp lệ: in ra "INVALID".

#Ràng buộc
#-10^4 ≤ w, h ≤ 10^4
#1 ≤ |color| ≤ 20


w, h, color = input().split()
w = int(w)
h = int(h)
if w > 0 and h > 0:
    chu_vi = 2 * (w + h)
    dien_tich = w * h
    mau = color.capitalize()
    print(chu_vi, dien_tich, mau)
else:
    print("INVALID")