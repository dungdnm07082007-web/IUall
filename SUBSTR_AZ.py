#ho một xâu S.
#Nhiệm vụ của bạn là hãy tìm xâu con dài nhất có thể sao cho xâu con này có ký tự bắt đầu là 'A' và kết thúc bởi ký tự 'Z'.

#Input:
#Gồm một dòng chứa xâu S có độ dài không quá 200000.
#Xâu chỉ gồm các chữ cái in hoa (A–Z).

#utput:
#In ra độ dài của xâu con dài nhất thỏa mãn điều kiện đã cho.


S = input().strip()
A = S.find('A')
Z = S.rfind('Z')
if A != -1 and Z != -1 and A <= Z:
    print(Z - A + 1)
else:
    print(0)