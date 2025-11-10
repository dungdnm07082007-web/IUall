#Kiểm tra một số nguyên dương n có phải là số Armstrong tổng quát với số mũ p cho trước hay không
#(Tổng các chữ số mũ p bằng chính số đó)

#Input: hai số nguyên dương n, p
#Output: boolean (true nếu tổng các chữ số mũ p bằng n, false nếu không)


n, p = list(map(int, input().split()))
so = 0
tong = n
while tong > 0:
    chu_so = tong % 10
    so += chu_so ** p
    tong //= 10
if so == n:
    print("True")
else:
    print("False")