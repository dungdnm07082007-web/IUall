#Ở một ngôi làng nhỏ, thầy Arin thích đặt các câu đố toán học cho học trò của mình. Hôm nay, thầy đưa ra một phép cộng kỳ lạ và nhờ các học sinh xác định xem phép tính đó có đúng hay không.

#Nhiệm Vụ
#Bạn được cung cấp một dòng gồm 5 giá trị theo dạng:
#A + B = C
#A, B, C là các số nguyên không âm.
#Nhiệm vụ của bạn là kiểm tra xem phép cộng A + B có bằng C hay không.

#Input
#Một dòng gồm 5 giá trị: A + B = C, cách nhau bởi dấu cách.

#Output
#Nếu A + B = C, in YES
#Ngược lại, in NO

#Ràng buộc
#0 ≤ A, B, C ≤ 10^9
#Phép cộng là số nguyên, không âm


s = input()
d = s.split()
a = int(d[0])
b = int(d[2])
c = int(d[4])
if a + b == c:
    print('YES')
else:
    print('NO')