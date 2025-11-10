#Ở xứ sở Numeria, nhà toán học trẻ Arin phát hiện một cỗ máy có thể chuyển đổi một số nguyên từ hệ thập phân sang bất kỳ hệ cơ số từ 2 đến 36. Nhiệm vụ của bạn là giúp Arin vận hành cỗ máy và tính toán kết quả chính xác.

#Nhiệm Vụ
#Nhập vào số lượng thử nghiệm t.
#Mỗi thử nghiệm gồm hai số nguyên n và k:
#n là số cần chuyển đổi.
#k là cơ số muốn chuyển đổi (2 ≤ k ≤ 36).
#Chuyển đổi n sang hệ cơ số k và in kết quả dưới dạng chuỗi, dùng các ký tự '0'-'9' cho giá trị 0–9 và 'A'-'Z' cho giá trị 10–35.
#In mỗi kết quả trên một dòng.

#Input
#Dòng đầu tiên: số nguyên t (1 ≤ t ≤ 100)
#t dòng tiếp theo, mỗi dòng chứa hai số nguyên n và k (0 ≤ n ≤ 10^9, 2 ≤ k ≤ 36)

#Output
#Mỗi dòng in ra kết quả chuyển đổi của từng thử nghiệm.


digit = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
t = int(input())
for _ in range(t):
    n, k = map(int, input().split()) 
    if n == 0:
        result = "0"
    else:
        result = ""
        temp_n = n      
        while temp_n > 0:
            remainder = temp_n % k
            result = digit[remainder] + result
            temp_n //= k          
    print(result)