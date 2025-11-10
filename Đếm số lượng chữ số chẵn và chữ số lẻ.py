#Đếm số lượng chữ số chẵn và chữ số lẻ trong một số nguyên dương.

#Input: một số nguyên dương n
#Output: một danh sách gồm 2 số [số_chẵn, số_lẻ]


n = input()
a = 0
b = 0
for i in range(len(n)):
    if int(n[i]) % 2 == 0:
        a += 1
    else:
        b += 1
print([a,b]) 