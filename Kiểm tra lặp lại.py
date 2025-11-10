#Kiểm tra xem một số nguyên dương n có chứa ít nhất một chữ số lặp lại liên tiếp hay không.

#Input: một số nguyên dương n
#Output: boolean (true nếu có chữ số lặp liên tiếp, false nếu không)

#Ràng buộc: Sử dụng vòng lặp và rẽ nhánh


n = input()
a = False
for i in range(len(n)):
    if n[i] in n[i+1:]:
        a = True
        break
if a:
    print("true")
else:
    print("false")