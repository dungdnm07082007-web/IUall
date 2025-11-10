#Tại Học viện Numeria, pháp sư Digitus phát hiện một loại phép thuật dựa trên số nguyên tố:
#Một chuỗi số được coi là “mạnh mẽ” nếu độ dài của chuỗi là một số nguyên tố và số lượng chữ số nguyên tố trong chuỗi lớn hơn số chữ số không nguyên tố.
#Bạn, học trò pháp sư Lyra, được giao nhiệm vụ xác định những chuỗi số mạnh mẽ này.

#Nhiệm Vụ
#Cho t chuỗi số:
#Kiểm tra mỗi chuỗi theo hai điều kiện:
#Độ dài chuỗi là số nguyên tố.
#Số lượng chữ số nguyên tố (2, 3, 5, 7) lớn hơn số chữ số không nguyên tố.
#Nếu cả hai điều kiện đúng → in "YES", ngược lại → in "NO".

#Input
#Dòng 1: số nguyên t (1 ≤ t ≤ 100) — số chuỗi
#t dòng tiếp theo: mỗi dòng là một chuỗi số n (1 ≤ |n| ≤ 1000, chỉ chứa chữ số 0–9)

#Output
#t dòng, mỗi dòng "YES" hoặc "NO" tương ứng với chuỗi đó.

#Ràng buộc
#1 ≤ t ≤ 100
#1 ≤ |n| ≤ 1000
#Chuỗi chỉ chứa các chữ số 0–9


def isprime(n):
    if n < 2: return False  
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False    
    return True
def check(string):
    size = len(string)
    cnt_isprime = 0
    for ch in string:
        if isprime(int(ch)):
            cnt_isprime += 1   
    not_isprime = size - cnt_isprime
    if isprime(size) and  cnt_isprime > not_isprime:
        return True
    return False
t = int(input())
while t > 0:
    string = input()
    if check(string):
        print("YES")
    else:
        print("NO")
    t -= 1