#Câu chuyện:
#Ở Trường Tiểu học Nam Dương, cô Lan giao cho học sinh một bài toán về tổng các phân số với các mẫu số lẻ hoặc chẵn. Các em phải tính tổng các phân số từ 1 đến n theo một quy tắc:
#Nếu n là số lẻ, tính tổng các phân số có mẫu số lẻ từ 1 đến n.
#Nếu n là số chẵn, tính tổng các phân số có mẫu số chẵn từ 2 đến n.
#Bạn được giao nhiệm vụ viết chương trình giúp cô Lan tính đúng tổng với 6 chữ số thập phân.

#Nhiệm vụ
#Viết chương trình tính tổng các phân số theo quy tắc trên.

#Input
#Dòng đầu tiên: số nguyên t (1 ≤ t ≤ 100) – số lượng test case
#Tiếp theo t dòng, mỗi dòng chứa một số nguyên n (1 ≤ n ≤ 10^6)

#Output
#Với mỗi test case, in ra tổng các phân số, làm tròn 6 chữ số thập phân


t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        total = sum(1/x for x in range(2, n+1, 2))
    else:
        total = sum(1/x for x in range(1, n+1, 2))
    print(f"{total:.6f}")