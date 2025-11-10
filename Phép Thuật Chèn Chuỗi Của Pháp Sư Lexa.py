#Tại vương quốc Lexiconia, pháp sư Lexa phát hiện ra một phép thuật giúp chèn một chuỗi vào một vị trí xác định trong chuỗi khác.
#Bạn, học trò pháp sư Kael, được giao nhiệm vụ thực hiện phép thuật này để tạo ra chuỗi mới từ hai chuỗi cho trước.

#Nhiệm Vụ
#Cho hai chuỗi a và b, và một số nguyên p:
#Chèn chuỗi b vào chuỗi a tại vị trí p (1-based).
#Vị trí 1 → trước ký tự đầu tiên
#Vị trí len(a)+1 → sau ký tự cuối cùng
#In kết quả chuỗi mới.

#Input
#Dòng 1: chuỗi a (1 ≤ |a| ≤ 10^5)
#Dòng 2: chuỗi b (1 ≤ |b| ≤ 10^5)
#Dòng 3: số nguyên p (1 ≤ p ≤ |a|+1)

#Output
#Dòng duy nhất: chuỗi mới sau khi chèn b vào a tại vị trí p

#Ràng buộc
#1 ≤ |a|, |b| ≤ 10^5
#1 ≤ p ≤ |a|+1


a = input().strip()
b = input().strip()
p = int(input().strip())
index = p - 1
new = a[:index] + b + a[index:]
print(new)