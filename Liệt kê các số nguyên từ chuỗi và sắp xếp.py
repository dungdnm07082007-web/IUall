#Câu chuyện: Trong một xưởng phép thuật, pháp sư Minh có nhiều chuỗi kỳ diệu gồm các chữ cái và số. Minh muốn liệt kê tất cả các số nguyên xuất hiện trong các chuỗi này và sắp xếp chúng theo thứ tự tăng dần để dễ dàng sử dụng trong các phép tính ma thuật. Bạn sẽ giúp Minh hoàn thành nhiệm vụ này.
#Nhiệm vụ: Viết chương trình đọc n chuỗi, trích xuất tất cả các số nguyên xuất hiện trong các chuỗi và in ra chúng theo thứ tự tăng dần.

#Một số nguyên là dãy liên tiếp các chữ số (0-9).
#Các chữ cái (a-z, A-Z) ngắt quãng số, nghĩa là số trước chữ cái và số sau chữ cái được xem là hai số riêng biệt.
#Sắp xếp tất cả các số tìm được theo thứ tự tăng dần trước khi in ra.

#Input:
#Dòng đầu tiên là số nguyên n — số lượng chuỗi.
#n dòng tiếp theo, mỗi dòng là một chuỗi gồm chữ cái và chữ số.

#Output:
#In tất cả các số nguyên tìm được trên các dòng, mỗi số một dòng, theo thứ tự tăng dần.

#Giải thích:
#Chuỗi ab12cd3 → số nguyên: 12, 3
#Chuỗi x9y8 → số nguyên: 9, 8
#Chuỗi p100q50 → số nguyên: 100, 50
#Tất cả số: 3, 8, 9, 12, 50, 100 → sắp xếp tăng dần
#
# Ràng buộc:
#1 ≤ n ≤ 100
#Chuỗi có độ dài ≤ 1000 ký tự
#Chỉ gồm chữ cái (a-z, A-Z) và chữ số (0-9)


n = int(input())
numbers = []
for _ in range(n):
    s = input()
    num = ''
    for ch in s:
        if ch.isdigit():
            num += ch
        else:
            if num != '':
                numbers.append(int(num))
                num = ''
    if num != '':
        numbers.append(int(num))
numbers.sort()
for x in numbers:
    print(x)