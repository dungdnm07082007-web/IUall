#Tại vương quốc Numeria, pháp sư Numerion sở hữu một phép thuật đặc biệt gọi là Phép Lật Ngược Số.
#Mỗi lần thực hiện phép thuật, Numerion chọn một số n và cộng số đó với phiên bản đảo ngược các chữ số của nó.
#Phép thuật được thực hiện lặp đi lặp lại cho đến khi số mới thu được chia hết cho 7.
#Bạn, học trò pháp sư Lyra, được giao nhiệm vụ tìm kết quả cuối cùng của mỗi số sau khi thực hiện phép thuật.

#Nhiệm Vụ
#Cho t thử thách, mỗi thử thách là một số nguyên n. Với mỗi n, thực hiện lặp lại:
#Nếu n chia hết cho 7 → dừng
#Ngược lại → n = n + đảo ngược các chữ số của n
#Lặp lại cho đến khi n chia hết cho 7
#In ra số cuối cùng sau khi phép thuật hoàn tất.

#Input
#Dòng 1: Số nguyên t — số lượng thử thách
#t dòng tiếp theo: mỗi dòng 1 số nguyên n (1 ≤ n ≤ 10^9)

#Output
#Với mỗi thử thách, in ra số cuối cùng sau khi thực hiện phép thuật, mỗi số trên một dòng.

#Ràng buộc
#1 ≤ t ≤ 1000
#1 ≤ n ≤ 10^9


t = int(input())
while t > 0:
    nums = int(input())
    while nums % 7 != 0:
        string = str(nums)
        new_nums = int(string[::-1])
        nums += new_nums
    print(nums)
    t -= 1