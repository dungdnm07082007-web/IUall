#Trong vương quốc Verdantia, có một khu rừng cổ xưa được gọi là Rừng Cổ Thụ Thầm Lặng. Người duy nhất có thể dẫn đoàn lữ khách đi qua rừng là Lina, một nữ hướng dẫn viên dày dạn kinh nghiệm, biết chính xác số bước mà mỗi lữ khách phải đi để đến được Cổng Bích Ngọc.
#Mỗi bước đi của lữ khách được đánh dấu bằng một ký hiệu trong chuỗi s, thể hiện từng trạm dừng trên đường mòn. Lina cần xác định số bước di chuyển thực tế, tức là tổng số trạm dừng trừ đi trạm xuất phát đầu tiên.

#Nhiệm vụ
#Nhập vào một chuỗi s, mỗi ký tự biểu thị một trạm dừng.
#Tính và in ra số bước đi thực tế qua rừng, bằng độ dài chuỗi trừ 1.

#Dữ liệu vào
#Một dòng: chuỗi s (độ dài ≥ 1).

#Dữ liệu ra
#Một số nguyên duy nhất — số bước di chuyển qua rừng.


s = input()
dai = len(s)
buoc = dai - 1
print(buoc)