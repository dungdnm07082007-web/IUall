#Đề bài: Tính tổng và tích các chữ số trong chuỗi
#Bạn được cung cấp một số lượng chuỗi số nguyên. Nhiệm vụ của bạn là tính:
#Tổng các chữ số ở vị trí chẵn (vị trí 0, 2, 4, ... theo chỉ số từ 0).
#Tích các chữ số ở vị trí lẻ (vị trí 1, 3, 5, ... theo chỉ số từ 0). Nếu tất cả các chữ số ở vị trí lẻ là số 0, thì tích bằng 0.

#Đầu vào:
#Dòng đầu tiên chứa một số nguyên t (1 ≤ t ≤ 1000): số lượng chuỗi số.
#t dòng tiếp theo, mỗi dòng chứa một chuỗi ký tự số.

#Đầu ra:
#Đối với mỗi chuỗi, in ra hai số nguyên trên một dòng: tổng các chữ số ở vị trí chẵn và tích các chữ số ở vị trí lẻ.

#Chú ý:
#Nếu một chuỗi không có chữ số lẻ nào khác 0, thì in ra tích bằng 0.


t = int(input())
for _ in range(t):
    s = input().strip()
    tong = 0
    tich = 1
    for i in range(len(s)):
        d = int(s[i])
        if i % 2 == 0:
            tong += d
        else:
            if d != 0:
                tich *= d           
    print(tong,tich)