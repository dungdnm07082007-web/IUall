#Đề bài: Tại vương quốc Ánh Ngôn, có một vị học giả tên Lữ Tự Ngôn, người chuyên nghiên cứu về ngôn ngữ cổ xưa. Một ngày nọ, ông nhận được một bức thư bí ẩn từ vùng đất Hoang Ngữ. Bức thư chỉ gồm một chuỗi ký tự dài, được viết liền nhau nhưng thực chất là các từ riêng biệt được ngăn cách bởi khoảng trắng.
#Nhiệm vụ của bạn là giúp Lữ Tự Ngôn tách từng từ trong chuỗi ký tự đó và in ra mỗi từ trên một dòng, để ông có thể nghiên cứu và giải mã nội dung bức thư.

#Yêu cầu:
#Nhập vào một dòng chứa nhiều từ, mỗi từ cách nhau bởi dấu cách.
#In ra mỗi từ trên một dòng riêng biệt theo đúng thứ tự xuất hiện.

#Ràng buộc:
#1 ≤ số lượng từ trong chuỗi ≤ 10⁵
#Mỗi từ có độ dài ≤ 100 ký tự
#Chuỗi chỉ bao gồm chữ cái và dấu cách hợp lệ


lst = list(map(str, input().split()))
for index, nums in enumerate(lst):
    print(nums, end = "\n")                     