#Trong xưởng rèn Zorak, có một dãy thanh kiếm được đánh số từ 1 đến n. Mỗi thanh kiếm có một chỉ số sức mạnh, và được phân loại:
#Lẻ: Thanh kiếm huyền thoại.
#Chẵn: Thanh kiếm thường.
#Thợ rèn Zorak muốn xếp lại thanh kiếm theo một chiến lược đặc biệt trước khi đưa chúng vào kho:
#Các thanh kiếm huyền thoại (lẻ) được sắp theo thứ tự tăng dần nhưng đặt vào vị trí ban đầu của chúng.
#Các thanh kiếm thường (chẵn) được sắp theo thứ tự giảm dần và cũng đặt vào vị trí ban đầu của chúng.

#Nhiệm vụ của bạn là viết chương trình giúp Zorak sắp xếp thanh kiếm theo đúng chiến lược này.

#Input
#Dòng đầu chứa số nguyên n — số lượng thanh kiếm.
#Dòng tiếp theo chứa n số nguyên a1, a2, …, an — chỉ số sức mạnh của từng thanh kiếm.

#Output
#In ra n số, là dãy thanh kiếm sau khi được sắp xếp theo chiến lược của Zorak.


n = int(input())
kiem = list(map(int, input().split()))
huyenthoai = []
thuong = []
for i in range(n):
    if kiem[i] % 2 == 1:
        huyenthoai.append(kiem[i])
    else:
        thuong.append(kiem[i])
huyenthoai.sort(reverse=True)
thuong.sort()
result = []
index_huyenthoai = 0
index_thuong = 0
for i in range (n):
    if kiem[i] % 2 == 1:
        result.append(huyenthoai[index_huyenthoai]) 
        index_huyenthoai += 1
    else:
        result.append(thuong[index_thuong])
        index_thuong += 1
print(" ".join(map(str, result)))