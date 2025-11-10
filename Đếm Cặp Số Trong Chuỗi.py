#Câu chuyện:
#Trong một thị trấn nhỏ, cậu bé Nam nhận được một chuỗi dài gồm các chữ số. Nam muốn xem tất cả các cặp số liên tiếp xuất hiện trong chuỗi để ghi chú lại các cặp số đó theo thứ tự tăng dần.
#Nam cần bạn giúp cậu làm việc này.

#Nhiệm vụ
#Cho một chuỗi số a có độ dài chẵn. Chia chuỗi thành các cặp số liên tiếp, đếm số lần xuất hiện của mỗi cặp, và in ra danh sách các cặp số khác nhau theo thứ tự tăng dần.

#Input
#Một dòng duy nhất chứa chuỗi a gồm các chữ số (độ dài chẵn, 2 ≤ |a| ≤ 1000)

#Output
#In ra tất cả các cặp số khác nhau theo thứ tự tăng dần, cách nhau bằng một khoảng trắng


a = input().strip()
pairs = set()
for i in range(0, len(a), 2):
    pair = a[i:i+2]
    pairs.add(pair)
    gtnn = sorted(pairs)
print(" ".join(gtnn))