#Trong một làng phép thuật, phù thủy Numina phát hiện một con số thần kỳ s. Cô ấy muốn biết số lần biến đổi cần thiết để con số trở thành một chữ số duy nhất.
#Biến đổi được định nghĩa như sau:
#Cộng tất cả các chữ số của số hiện tại để tạo ra một số mới.
#Lặp lại quá trình này cho đến khi số còn lại chỉ có một chữ số.
#Nhiệm vụ của bạn là tính số lần biến đổi cần thiết.

#Input
#Một dòng chứa chuỗi số nguyên s (không chứa dấu âm, không có số 0 đứng đầu trừ khi s là "0").

#Output
#Một số nguyên — số lần biến đổi cần thiết để s trở thành một chữ số duy nhất.


s = input().strip()
tong = 0
if len(s) == 1:
    print(tong)
else:
    while len(s) > 1:
        n = sum(int(so) for so in s)
        s = str(n)
        tong +=1
    print(tong)
