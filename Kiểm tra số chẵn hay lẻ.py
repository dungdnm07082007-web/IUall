#Kiểm tra xem một số nguyên là số chẵn hay số lẻ.

#Input: Một số nguyên n.
#Output: Thông báo cho biết số vừa nhập là số chẵn hay số lẻ.


n = int(input())
if n % 2 == 0:
    print("So ban nhap la so chan")
else:
    print("So ban nhap la so le")