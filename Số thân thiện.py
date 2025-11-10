#Số tự nhiên có rất nhiều tính chất thú vị. Ví dụ với số 23, số đảo ngược của nó là 32. Hai số này có ước chung lớn nhất là 1. Những số như thế được gọi là số thân thiện, tức là số 23 được gọi là số thân thiện, số 32 cũng được gọi là số thân thiện.
#Hãy nhập vào 2 số nguyên a, b (1 =< a =< b =< 10^6). Hãy đếm xem trong khoảng từ a đến b (kể cả a và b) có bao nhiêu số thân thiện.

#Input
#Bao gồm một dòng chứa 2 số a, b. Hai số được cách nhau bằng một khoảng trắng.

#Output
#Bao gồm một dòng là kết quả của bài toán.


import sys
a, b = map(int, sys.stdin.read().split())
def ucln(x, y):
    while y:
        x, y = y, x % y
    return x
def dao_nguoc(n):
    reversed_n = 0
    while n > 0:
        chu_so = n % 10
        reversed_n = reversed_n * 10 + chu_so
        n //= 10
    return reversed_n
so_luong_than_thien = 0
for i in range(a, b + 1):
    i_dao_nguoc = dao_nguoc(i)
    ket_qua_ucln = ucln(i, i_dao_nguoc)
    if ket_qua_ucln == 1:
        so_luong_than_thien += 1
print(so_luong_than_thien)
