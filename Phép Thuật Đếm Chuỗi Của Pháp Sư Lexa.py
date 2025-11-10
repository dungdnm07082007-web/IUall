#Tại vương quốc Lexiconia, pháp sư Lexa đang nghiên cứu một phép thuật để đếm số lần xuất hiện của một chuỗi con trong văn bản.
#Mỗi phép thuật yêu cầu xác định số lần một chuỗi con xuất hiện trong chuỗi chính.
#Bạn, học trò pháp sư Kael, được giao nhiệm vụ thực hiện phép thuật này.

#Nhiệm Vụ
#Cho t phép thuật, mỗi phép thuật gồm:
#Nhập chuỗi chính s
#Nhập chuỗi con n
#Tính và in số lần chuỗi con n xuất hiện trong chuỗi s

#Input
#Dòng 1: số nguyên t (1 ≤ t ≤ 1000) — số phép thuật
#2×t dòng tiếp theo: mỗi phép thuật gồm:
#Dòng 1: chuỗi s (1 ≤ |s| ≤ 10^5)
#Dòng 2: chuỗi n (1 ≤ |n| ≤ 10^3)

#Output
#t dòng, mỗi dòng một số nguyên: số lần chuỗi con n xuất hiện trong s

#Ràng buộc
#1 ≤ t ≤ 1000
#1 ≤ |s| ≤ 10^5
#1 ≤ |n| ≤ 10^3


t = int(input())
for _ in range(t):
    s = input().strip()
    n = input().strip()
    count = 0
    i = 0
    while i <= len(s) - len(n):
        if s[i:i+len(n)] == n:
            count += 1
            i += len(n)
        else:
            i += 1
    print(count)