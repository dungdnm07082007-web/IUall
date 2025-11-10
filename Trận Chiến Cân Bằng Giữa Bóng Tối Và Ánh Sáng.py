#**Cuộc So Tài Giữa Hai Đội Chiến Binh **
#Bối cảnh
#Tại Vương quốc Athelor, mỗi năm sẽ diễn ra Đại Chiến Xếp Hạng, nơi các chiến binh trẻ từ khắp nơi tụ họp về chiến trường Thung Lũng Cân Bằng. Hai đội tham chiến trong mỗi trận:
#Đội Hắc Ảnh – sở hữu chiến binh nhanh nhẹn, mang sức mạnh từ bóng tối. Danh sách sức mạnh chiến binh của họ được biểu diễn bởi dãy số A.
#Đội Quang Minh – lực lượng ánh sáng, mỗi chiến binh mang trong mình năng lượng thuần khiết. Sức mạnh chiến binh của họ được biểu diễn bởi dãy số B.
#Trước khi bắt đầu quyết đấu, hai đội sẽ xếp đội hình theo thứ tự tăng dần sức mạnh. Cuộc chiến chỉ được xem là công bằng và chấp nhận nếu mỗi chiến binh của Đội Hắc Ảnh (sau khi xếp lại thứ tự) không mạnh hơn chiến binh tương ứng của Đội Quang Minh.

#Nhiệm vụ của bạn là xác định xem trận đấu có được phê duyệt hay không.

#Yêu cầu
#Với mỗi trận đấu:
#Nhập số lượng chiến binh n.
#Nhập danh sách sức mạnh của Đội Hắc Ảnh A (n số nguyên).
#Nhập danh sách sức mạnh của Đội Quang Minh B (n số nguyên).
#Sau khi sắp xếp cả hai danh sách theo thứ tự tăng dần, nếu với mọi vị trí i ta có A[i] ≤ B[i], in ra "YES", ngược lại in "NO".

#Input
#Dòng đầu: số nguyên t – số trận đấu.

#Với mỗi trận đấu:
#Dòng 1: số nguyên n
#Dòng 2: dãy A gồm n số nguyên
#Dòng 3: dãy B gồm n số nguyên

#Output
#Với mỗi trận đấu, in ra "YES" hoặc "NO".


t = int(input())
while t > 0:
    case = int(input())   
    lsta = list(map(int, input().split()))
    lstb = list(map(int, input().split()))
    lsta.sort()
    lstb.sort()
    check = True
    for i in range(0, len(lsta)):
        if lsta[i] > lstb[i]:
            check = False
    if check:
        print("YES")
    else:
        print("NO")  
    t -= 1