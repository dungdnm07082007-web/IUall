#Trong thế giới ảo diệu của vũ trụ Among Numbers, pháp sư Amogus nắm giữ những con số quyền năng. Những con số này chỉ xuất hiện khi người chơi nhập đúng "mật khẩu số", và sẽ tiết lộ giá trị bí mật tương ứng.

#Nhiệm vụ
#Người chơi nhập một số nguyên n.

#Nếu n bằng một trong các số bí mật, chương trình sẽ in ra giá trị tương ứng:
#n	Giá trị in ra
#2458	307869816
#122158	15075958678
#415764	50727379000
#920709	113174333716
#Nếu n = 1000000, người chơi phải nhập thêm một số nguyên k. Giá trị in ra phụ thuộc vào k:
#k	Giá trị in ra
#2	232078603753
#Khác	9983741831
#Nếu n không thuộc các số trên, không có giá trị nào được in ra.

#Input
#n [k] # Chỉ khi n = 1000000
#n — số nguyên (0 < n ≤ 10^7)
#k — số nguyên (chỉ nhập khi n = 1000000)

#Output
#Giá trị tương ứng với n và k theo bảng trên.
#Nếu n không khớp, in không gì cả.


n = int(input())
so = {
    2458: 307869816,
    122158: 15075958678,
    415764: 50727379000,
    920709: 113174333716
}
if n in so:
    print(so[n])
elif n == 1000000:
    k = int(input())
    if k == 2:
        print(232078603753)
    else:
        print(9983741831)