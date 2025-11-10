#Remove All Adjacent Duplicates In String: Cho một chuỗi s gồm các chữ cái thường trong tiếng Anh. Một lần loại bỏ trùng lặp là chọn hai ký tự liền kề và giống nhau rồi xóa chúng. Ta lặp lại việc loại bỏ cho đến khi không thể tiếp tục. Trả về chuỗi cuối cùng sau khi tất cả các lần loại bỏ hoàn tất. Có thể chứng minh rằng kết quả là duy nhất.


s = input()
day = []
for ch in s:
    if day and day[-1] == ch:
        day.pop()
    else:
        day.append(ch)
tong = ''.join(day)
print(tong)