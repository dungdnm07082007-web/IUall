#Bài toán: Tính tổng các chữ số của một số
#Mô tả:
#Nhập một số nguyên n và tính tổng các chữ số của nó.

#Input:
#Một số nguyên n.

#Output:
#Một số nguyên duy nhất là tổng các chữ số của n.


n_str = input()
if n_str.startswith('-'):
    n_str = n_str[1:]
tong = sum(int(chu_so) for chu_so in n_str)
print(tong)