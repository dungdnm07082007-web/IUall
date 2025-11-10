#Bài toán: Đếm số lượng nguyên âm trong chuỗi
#Mô tả:
#Nhập một chuỗi ký tự và đếm số lượng nguyên âm (a, e, i, o, u) có trong chuỗi.
#Không phân biệt chữ hoa và chữ thường.

#Input:
#Một chuỗi ký tự.

#Output:
#Một số nguyên duy nhất là số lượng nguyên âm trong chuỗi.


n = input().lower()
t = [x for x in n if x in "aeiou"]
print(len(t))