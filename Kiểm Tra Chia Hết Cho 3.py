#Trong vương quốc ModuloLand, pháp sư TriDivis đang luyện phép thuật. Nhiệm vụ của cậu là kiểm tra xem các con số mà cậu tìm được có chia hết cho 3 hay không để mở ra cánh cổng phép thuật.
#Cậu nhận được t số, với mỗi số, bạn cần xác định xem số đó có chia hết cho 3 không.
#Nếu số chia hết cho 3, in "YES".
#Nếu không chia hết cho 3, in "NO".

#Input
#Dòng đầu: số nguyên t — số lượng số cần kiểm tra.
#Với mỗi test case:
#Dòng duy nhất chứa số nguyên n.

#Output
#Với mỗi số, in "YES" nếu chia hết cho 3, "NO" nếu không chia hết.

#Ràng buộc
#1 ≤ t ≤ 1000
#0 ≤ n ≤ 10^9


t = int(input())
for i in range(t):
    n = int(input())
    if n % 3 == 0:
        print("YES")
    else:
        print("NO")