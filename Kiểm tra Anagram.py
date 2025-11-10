#Mô tả:
#Kiểm tra xem hai chuỗi s và t có phải là anagram của nhau hay không.
#Hai chuỗi là anagram nếu chúng chứa cùng các ký tự với cùng số lần xuất hiện.

#Input
#s, t — hai chuỗi chỉ chứa chữ cái thường
#Ràng buộc:
#1 <= |s|, |t| <= 5 * 10^4

#Output
#true nếu t là anagram của s
#false nếu không

#Constraints
#Chỉ chứa chữ cái thường (a–z)


s = input()
s2 = input()
set_1 = set(x for x in s)
set_2 = set(y for y in s2)
print('true' if set_1 == set_2 else 'false')