#Tại Vương quốc Saphira, có một cuộn sổ ghi chép tất cả các số hiệu công dân từ 1 trở đi. Tuy nhiên, trong một trận đại hồng thủy, một số bản ghi đã bị thất lạc.
#Thủ thư hoàng gia Elden được giao nhiệm vụ phục hồi lại số hiệu bị mất nhỏ nhất trong danh sách. Ông nhờ bạn giúp viết một chương trình để tìm ra số nguyên dương nhỏ nhất không xuất hiện trong danh sách đã cho.

#Input
#Dòng đầu chứa số nguyên n — số lượng số trong danh sách.
#Dòng tiếp theo chứa n số nguyên a1, a2, ..., an.

#Output
#In ra số nguyên dương nhỏ nhất không xuất hiện trong danh sách.


n = int(input())
day_so = list(map(int, input().split()))
so_hieu = set(day_so)
so_min = 1
while so_min in so_hieu:
    so_min += 1
print(so_min)