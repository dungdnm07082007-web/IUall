#Đề bài: Kiểm tra số nguyên tố của 4 chữ số cuối

#Bạn được cung cấp t chuỗi số nguyên. Nhiệm vụ của bạn là kiểm tra xem 4 chữ số cuối cùng của mỗi chuỗi số có tạo thành một số nguyên tố hay không. Nếu 4 chữ số cuối là một số nguyên tố, in ra "YES", ngược lại in ra "NO".

#Đầu vào:
#Dòng đầu tiên chứa số nguyên t (1 ≤ t ≤ 1000): số lượng chuỗi số.
#t dòng tiếp theo, mỗi dòng chứa một chuỗi ký tự số.

#Đầu ra:
#Đối với mỗi chuỗi số, in ra "YES" nếu 4 chữ số cuối tạo thành một số nguyên tố, in ra "NO" nếu không phải là số nguyên tố.

#Chú ý:
#Nếu chuỗi có ít hơn 4 chữ số, hãy kiểm tra toàn bộ số đó.


def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
t = int(input())
for _ in range(t):
    S = input().strip()
    if len(S) < 4:
        sub_S = S
    else:
        sub_S = S[-4:]
    if not sub_S:
        print("NO")
        continue
    num = int(sub_S)
    if is_prime(num):
        print("YES")
    else:
        print("NO")