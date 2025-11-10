#Trong một chiều không gian song song, có một hội bí ẩn mang tên “Order of ඞ”, gồm những học giả điên cuồng nghiên cứu về các con số hoàn hảo — những con số có khả năng chia đều cho nhiều số khác một cách kỳ lạ.
#Người đứng đầu hội, Giáo Chủ S, đang giữ một danh sách những “số siêu chia hết” — dãy các con số kỳ bí được sắp xếp theo thứ tự tăng dần. Mỗi con số trong dãy này được cho là chứa “sức mạnh cân bằng của vũ trụ toán học”.
#Một ngày nọ, học giả trẻ Lior được giao nhiệm vụ kiểm tra sức mạnh của dãy số này. Với mỗi con số n mà Lior nhận được, cậu phải tìm trong danh sách của Giáo Chủ S số nhỏ nhất lớn hơn hoặc bằng n, và báo lại kết quả.
#Nếu không tồn tại con số nào như vậy, Lior phải giữ im lặng — vũ trụ không cho phép nói dối về các con số hoàn hảo.

#Nhiệm vụ
#Cho một số nguyên t — số lượng câu hỏi. Mỗi câu hỏi chứa một số nguyên n. Với mỗi n, hãy in ra số nhỏ nhất trong danh sách cố định của Giáo Chủ S lớn hơn hoặc bằng n.

#Danh sách số của Giáo Chủ S
#[1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 554400, 665280, 720720, 1081080, 1441440, 2162160, 2882880, 3603600, 4324320, 6486480, 7207200, 8648640, 10810800]

#Input
#Dòng đầu chứa số nguyên t — số lượng truy vấn.
#t dòng tiếp theo, mỗi dòng chứa một số nguyên n.

#Output
#Với mỗi truy vấn, in ra số nhỏ nhất trong danh sách của Giáo Chủ S lớn hơn hoặc bằng n.


t = int(input())
ds = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 554400, 665280, 720720, 1081080, 1441440, 2162160, 2882880, 3603600, 4324320, 6486480, 7207200, 8648640, 10810800]
for _ in range(t):
    n = int(input())
    ket_qua = -1
    for x in ds:
        if x >= n:
            ket_qua = x
            break
    print(ket_qua)