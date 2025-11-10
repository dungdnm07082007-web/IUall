#Trong vương quốc Algoland, mỗi năm diễn ra cuộc thi sức mạnh giữa hai đội A và B. Mỗi đội có n thành viên, mỗi thành viên có một chỉ số sức mạnh.

#Nhiệm vụ của bạn là so sánh hai đội để xác định xem đội A có thể sắp xếp các thành viên sao cho mỗi thành viên không yếu hơn đối thủ cùng vị trí của đội B.
#Nếu tồn tại cách sắp xếp đội A thỏa điều kiện a[i] ≤ b[i] với tất cả i (sau khi sắp xếp tăng dần), in "YES".
#Ngược lại, in "NO".

#Input
#Dòng đầu: số nguyên t — số lượng test case.
#Với mỗi test case:
#Dòng đầu: số nguyên n — số lượng thành viên mỗi đội.
#Dòng thứ hai: n số nguyên a1 a2 ... an — chỉ số sức mạnh của đội A.
#Dòng thứ ba: n số nguyên b1 b2 ... bn — chỉ số sức mạnh của đội B.

#Output
#Với mỗi test case, in "YES" hoặc "NO" theo điều kiện trên.


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split())) 
    b = list(map(int, input().split())) 
    a.sort()
    b.sort()
    can_win = all(a[i] <= b[i] for i in range(n))
    print("YES" if can_win else "NO")