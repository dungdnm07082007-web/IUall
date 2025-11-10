#Trong vương quốc Alpinia, vận động viên trẻ Arin tham gia một cuộc thi leo núi đặc biệt. Cuộc thi gồm n ngọn núi, mỗi ngọn núi có độ cao và độ khó nhất định. Arin muốn chọn một dãy ngọn núi để leo theo thứ tự sao cho:
#Độ cao của các ngọn núi leo lên luôn tăng dần.
#Độ khó của các ngọn núi leo lên luôn giảm dần.

#Nhiệm vụ của bạn là xác định số lượng lớn nhất các ngọn núi mà Arin có thể leo theo quy tắc trên.

#Input
#Dòng đầu tiên chứa một số nguyên t (1 ≤ t ≤ 10) – số bộ dữ liệu.
#Với mỗi bộ dữ liệu:
#Dòng đầu tiên chứa số nguyên n (1 ≤ n ≤ 1000) – số ngọn núi.
#n dòng tiếp theo, mỗi dòng chứa hai số thực a_i và b_i (1 ≤ a_i, b_i ≤ 10^6), lần lượt là độ cao và độ khó của ngọn núi thứ i.

#Output
#Với mỗi bộ dữ liệu, in ra số nguyên – số lượng lớn nhất các ngọn núi mà Arin có thể leo theo quy tắc.


t = int(input())
for _ in range(t):
    nui = int(input())     
    ds_nui = []   
    for i in range(nui):
        dl = input().split()
        cao = float(dl[0]) 
        kho = float(dl[1]) 
        ds_nui.append((cao, kho))
    if nui == 0:
        print(0)
        continue  
    dp = [1] * nui
    dai_max = 0
    for i in range(nui):
        cao_i, kho_i = ds_nui[i]       
        for j in range(i):
            cao_j, kho_j = ds_nui[j]            
            if cao_j < cao_i and kho_j > kho_i:
                dp[i] = max(dp[i], dp[j] + 1)       
        dai_max = max(dai_max, dp[i])
    print(dai_max)
