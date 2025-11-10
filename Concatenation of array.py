#Cho một mảng số nguyên nums có độ dài n. Bạn cần tạo một mảng ans có độ dài 2n sao cho:
#ans[i] == nums[i] và
#ans[i + n] == nums[i] với mọi 0 <= i < n (chỉ số bắt đầu từ 0).
#Cụ thể, ans là kết quả của việc nối liền hai mảng nums.

#Hãy trả về mảng ans.


n = int(input())
so = list(map(int, input().split()))
noi = so + so
print(' '.join(map(str, noi)))
