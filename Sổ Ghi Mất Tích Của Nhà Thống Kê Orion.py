#Trong vương quốc Numeris, nhà thống kê hoàng gia Orion chịu trách nhiệm theo dõi toàn bộ số hiệu chiến binh của quân đội. Mỗi chiến binh được gán một số nguyên dương duy nhất.
#Tuy nhiên, sau cuộc di chuyển hỗn loạn trong đại chiến, một số bản ghi bị mất. Orion phải xác định những số hiệu nào bị thiếu trong dãy ghi chép hiện có.

#Nhiệm vụ của bạn là giúp Orion tìm ra tất cả các số nguyên dương nhỏ hơn hoặc bằng số hiệu lớn nhất mà chưa được ghi nhận. Nếu tất cả các số từ 1 đến số lớn nhất đều đã xuất hiện, hãy in ra "Excellent!".

#Input
#Dòng đầu tiên chứa số nguyên n — số lượng số hiệu cần nhập.
#Các dòng tiếp theo chứa các số nguyên, có thể được nhập trên nhiều dòng cho đến khi tổng cộng đủ n số.

#Output
#In ra tất cả các số nguyên dương chưa xuất hiện trong danh sách, mỗi số trên một dòng.
#Nếu không có số nào bị thiếu, in ra Excellent!.


n = int(input())
arr = list(map(int, input().split()))
missing = [i for i in range(1, max(arr)+1) if i not in arr]
print("Excellent!" if not missing else " ".join(map(str,missing)))
