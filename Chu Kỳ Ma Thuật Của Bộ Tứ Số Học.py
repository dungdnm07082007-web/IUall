#Trong vương quốc Numerion, có bốn hiền nhân cổ đại đại diện cho bốn nguyên tố: Lửa (Ignis), Nước (Aqua), Gió (Ventus) và Đất (Terra). Mỗi hiền nhân mang trong mình một chỉ số năng lượng là một số nguyên dương.
#Theo truyền thuyết, khi bốn hiền nhân thực hiện nghi thức cân bằng năng lượng, họ đồng thời biến đổi năng lượng của mình theo quy tắc:
#Năng lượng mới của mỗi hiền nhân được tính bằng độ chênh tuyệt đối giữa năng lượng hiện tại và của người kế tiếp trong vòng tròn (hiền nhân thứ tư được xem là liền kề hiền nhân thứ nhất).
#Nghi thức tiếp tục cho đến khi tất cả bốn hiền nhân có cùng một mức năng lượng. Khi đó, vòng cân bằng hoàn tất.

#Nhiệm vụ của bạn là xác định số lần biến đổi cần thiết để bốn hiền nhân đạt được trạng thái cân bằng.

#Input
#Chương trình nhận nhiều bộ dữ liệu, mỗi bộ gồm 4 số nguyên a1, a2, a3, a4 — năng lượng ban đầu của bốn hiền nhân. Kết thúc khi dòng nhập vào là 0 0 0 0.

#Output
#Với mỗi bộ dữ liệu, in ra một số nguyên — số lần biến đổi cần thiết để đạt được trạng thái cân bằng.


a1, a2, a3, a4 = map(int, input().split())
tong = 0
while not (a1 == 0 and a2 == 0 and a3 == 0 and a4 == 0):
    if a1 == a2 == a3 == a4:
        break
    b1 = abs(a1 - a2)
    b2 = abs(a2 - a3)
    b3 = abs(a3 - a4)
    b4 = abs(a4 - a1)
    a1, a2, a3, a4 = b1, b2, b3, b4
    tong = tong + 1
print(tong)