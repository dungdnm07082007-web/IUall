#Tại vương quốc Geometria, pháp sư Geometra có khả năng đo khoảng cách chính xác giữa hai điểm trên mặt phẳng ma thuật.
#Mỗi phép đo là một thử thách với hai điểm (x1, y1) và (x2, y2).
#Bạn, học trò pháp sư Lyra, được giao nhiệm vụ tính khoảng cách Euclid giữa hai điểm với độ chính xác cao.

#Nhiệm Vụ
#Cho t thử thách, mỗi thử thách gồm hai điểm:
#Nhập tọa độ hai điểm (x1, y1) và (x2, y2).
#Tính khoảng cách Euclid giữa hai điểm: [ d = \sqrt{(x1 - x2)^2 + (y1 - y2)^2} ]
#In kết quả với 4 chữ số thập phân.

#Input
#Dòng 1: số nguyên t (1 ≤ t ≤ 1000) — số thử thách
#t dòng tiếp theo, mỗi dòng 4 số thực:
#x1 y1 x2 y2
#-10^6 ≤ xi, yi ≤ 10^6

#Output
#Với mỗi thử thách, in một dòng: khoảng cách giữa hai điểm, làm tròn 4 chữ số thập phân.

#Ràng buộc
#1 ≤ t ≤ 1000
#-10^6 ≤ xi, yi ≤ 10^6


t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(float, input().split())
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    print(f"{d:.4f}")