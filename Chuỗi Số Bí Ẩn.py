#Trong một làng số học, thầy phù thủy Arion đưa cho bạn một dãy số nguyên. Ông có một trò chơi kỳ lạ: ông muốn bạn tạo ra một chuỗi mới từ dãy ban đầu theo luật sau:
#Bắt đầu với chuỗi rỗng b.
#Duyệt từng số i trong dãy gốc a:
#Nếu b rỗng, thêm i vào b.
#Ngược lại, nếu tổng i + b[-1] là chẵn, loại bỏ phần tử cuối cùng của b.
#Nếu tổng i + b[-1] là lẻ, thêm i vào b.
#Sau khi duyệt hết dãy, in độ dài cuối cùng của chuỗi b.

#Input
#Dòng đầu tiên: số nguyên n — số lượng phần tử của dãy.
#Dòng thứ hai: n số nguyên a1 a2 ... an — các phần tử của dãy.

#Output
#Một số nguyên: độ dài của chuỗi b sau khi thực hiện trò chơi.