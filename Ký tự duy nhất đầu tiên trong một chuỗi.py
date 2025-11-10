#Trả về chỉ số của ký tự đầu tiên không lặp lại trong chuỗi.

#Input
#Chuỗi s:
#Độ dài: 1 <= |s| <= 10^5
#Chỉ chứa các chữ cái thường (lowercase letters)

#Output
#Chỉ số (tính từ 0) của ký tự đầu tiên không lặp lại trong s, hoặc -1 nếu không tồn tại ký tự như vậy.

#Constraints
#Chuỗi s chỉ chứa các chữ cái thường (a-z).


string = input()
dct = {}
for index, ch in enumerate(string):
    if ch not in dct:
        dct[ch] = 1
    else:
        dct[ch] += 1
pos = 1000000000
for index, ch in enumerate(string):
    if dct[ch] == 1:
        pos = min(pos, index)
if pos == 1000000000:
    print(-1)
else:
    print(pos)