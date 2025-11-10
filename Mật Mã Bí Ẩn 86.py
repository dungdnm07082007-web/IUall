#Trong vương quốc công nghệ, thám tử số học Lira đang giải mã những chuỗi ký tự từ một máy tính cổ xưa. Một chuỗi được coi là chuỗi “bí ẩn 86” nếu hai ký tự cuối cùng của nó là “86”.
#Nhiệm vụ của bạn là giúp Lira kiểm tra các chuỗi và in "YES" nếu chuỗi đó là chuỗi bí ẩn 86, ngược lại in "NO".

#Input
#Dòng đầu tiên: số nguyên t — số lượng chuỗi cần kiểm tra.
#t dòng tiếp theo, mỗi dòng chứa một chuỗi s.

#Output
#Với mỗi chuỗi, in "YES" nếu hai ký tự cuối là "86", ngược lại in "NO".

#Ràng buộc
#1 ≤ t ≤ 100
#1 ≤ |s| ≤ 1000
#Chuỗi chỉ gồm các ký tự ASCII.


def kt(s):
    a = s[-2::]
    if len(s) < 2:
        return False
    elif a == '86':
        return True
    else:
        return False
n = int(input())
for i in range(n):
    s = input()
    if kt(s) == True:
        print('YES')
    else:
        print('NO')