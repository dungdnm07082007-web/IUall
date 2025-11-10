#Nhà sưu tầm Liora nổi tiếng khắp vùng với cuốn sổ lưu trữ những dấu ấn linh hồn – mỗi dấu ấn là một chuỗi ký tự duy nhất đại diện cho một linh hồn mà cô từng gặp trong chuyến hành trình xuyên qua các cõi. Tuy nhiên, trong sổ của cô luôn có một dấu ấn đặc biệt mang giá trị "-1" – dấu ấn khởi nguồn, không được tính vào số lượng thật sự.
#Giờ đây, Liora muốn biết có bao nhiêu dấu ấn khác nhau mà cô đã thu thập được, không kể dấu ấn đặc biệt đó.

#Yêu cầu
#Cho n chuỗi ký tự, mỗi chuỗi là một dấu ấn. Hãy xác định số lượng dấu ấn duy nhất trong các chuỗi đó, bỏ qua giá trị "-1".

#Input
#Dòng đầu chứa số nguyên n — số lượng dấu ấn được ghi lại.
#n dòng tiếp theo, mỗi dòng chứa một chuỗi ký tự đại diện cho một dấu ấn.

#Output
#In ra một số nguyên duy nhất là số lượng dấu ấn khác nhau (không tính "-1").


t = int(input())
mp = []
cnt = 0
while t > 0:
    string = input()
    if string not in mp and string != "-1":
        cnt += 1
        mp.append(string)
    t -= 1
print(cnt)

