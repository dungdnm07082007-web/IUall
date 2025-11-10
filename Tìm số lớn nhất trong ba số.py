#Tìm số lớn nhất trong ba số nguyên.

#Input
#Ba số nguyên a, b, c.

#Output
#Một số nguyên là giá trị lớn nhất trong ba số đã nhập.


a, b, c = map(int,input().split())
max_value = max (a, b, c)
print(max_value)