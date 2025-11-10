#Tại vương quốc Numeria, pháp sư Countius tổ chức một cuộc thi phép thuật giữa các học trò.
#Mỗi học trò được gán một con số may mắn trong khoảng từ 1 đến k.
#Pháp sư muốn tìm ra con số có số lần xuất hiện cao thứ hai trong danh sách, để trao phần thưởng đặc biệt.

#Nhiệm Vụ
#Nhập:
#Hai số nguyên n (số lượng học trò), k (giới hạn số may mắn).
#Dòng tiếp theo gồm n số nguyên a₁, a₂, ..., aₙ — số may mắn của từng học trò (1 ≤ aᵢ ≤ k).
#Xác định số may mắn xuất hiện nhiều thứ hai (theo tần suất) trong danh sách.
#Nếu không tồn tại, in "NONE".

#Input
#Dòng 1: hai số nguyên n, k (1 ≤ n ≤ 1000, 1 ≤ k ≤ 1000)
#Dòng 2: n số nguyên a₁ a₂ ... aₙ (1 ≤ aᵢ ≤ k)

#Output
#Số may mắn xuất hiện nhiều thứ hai trong danh sách, hoặc "NONE" nếu không tồn tại.


n, k = map(int, input().split())
a = list(map(int, input().split()))
q = {}
for num in a:
    q[num] = q.get(num, 0) + 1
q_values = sorted(set(q.values()), reverse=True)
if len(q_values) < 2:
    print("NONE")
else:
    second_q = q_values[1]
    luck = [num for num, f in q.items() if f == second_q]
    print(min(luck))