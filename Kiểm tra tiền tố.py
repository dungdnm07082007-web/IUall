#Kiểm tra chuỗi s có phải là tiền tố của chuỗi t hay không.

#Input: s,t
#Output: true/false
#Ràng buộc: 1 <= len(s), len(t) <= 10^4


s = input().strip()
t = input().strip()
if t.startswith(s):
    print("true")
else:
    print("false")