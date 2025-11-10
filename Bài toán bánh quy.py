#Giả sử bạn là một phụ huynh muốn cho con cái mình một số bánh quy, mỗi đứa trẻ chỉ nhận tối đa một chiếc bánh.
#Mỗi đứa trẻ i có một hệ số tham lam g[i], là kích thước tối thiểu của bánh quy mà đứa trẻ sẽ hài lòng.
#Mỗi bánh quy j có kích thước s[j].
#Nếu s[j] >= g[i], bánh quy j có thể được gán cho đứa trẻ i, và đứa trẻ đó sẽ hài lòng.

#Mục tiêu: tối đa hóa số lượng trẻ hài lòng.

#Input: hai mảng số nguyên g (tham lam) và s (kích thước bánh quy)

#Output: số lượng trẻ hài lòng tối đa


g_input = input()
s_input = input()
g = [int(x.strip()) for x in g_input.strip('[]').split(',') if x.strip()]
s = [int(x.strip()) for x in s_input.strip('[]').split(',') if x.strip()]
g.sort()
s.sort()
child_index = 0
cookie_index = 0
satisfied_count = 0
while child_index < len(g) and cookie_index < len(s):
    if s[cookie_index] >= g[child_index]:
        satisfied_count += 1
        child_index += 1
        cookie_index += 1
    else:
        cookie_index += 1
print(satisfied_count)