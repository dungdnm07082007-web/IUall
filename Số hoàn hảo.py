#Kiểm tra một số nguyên dương n có phải là số hoàn hảo hay không
#(Số hoàn hảo là số có tổng các ước số đúng bằng chính nó)

#Input: một số nguyên dương n
#Output: boolean (true nếu n là số hoàn hảo, false nếu không)


n = int(input())
if n <= 1:
    print("false")
else:
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    print("true" if total == n else "false")