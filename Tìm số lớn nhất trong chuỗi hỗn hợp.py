#Câu chuyện: Minh là một lập trình viên trẻ, đang xử lý các chuỗi dữ liệu bao gồm chữ cái và số. Minh muốn tìm số nguyên lớn nhất xuất hiện liên tiếp trong chuỗi, để phục vụ cho việc phân tích dữ liệu.

#Nhiệm vụ: Viết chương trình để:
#Nhận vào một số lượng chuỗi.
#Với mỗi chuỗi, tìm số nguyên lớn nhất xuất hiện liên tiếp trong chuỗi (số có thể có nhiều chữ số).
#In ra kết quả cho mỗi chuỗi.

#Input:
#Dòng đầu tiên: t — số lượng chuỗi cần kiểm tra.
#Tiếp theo t dòng, mỗi dòng là một chuỗi gồm chữ cái và chữ số.

#Output:
#Với mỗi chuỗi, in ra số nguyên lớn nhất xuất hiện liên tiếp trong chuỗi.


t = int(input())
for _ in range(t):
    n = input().strip()
    numbers = []
    num = ''
    for k in n:
        if k.isdigit():
            num += k
        else:
            if num != '':
                numbers.append(int(num))
                num = ''
    if num != "":
        numbers.append(int(num))
    print(max(numbers))