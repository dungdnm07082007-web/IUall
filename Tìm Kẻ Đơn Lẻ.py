#Trong vương quốc số học, người giám hộ Arithmos có một tập hợp các viên đá thần kỳ, mỗi viên đá được đánh số. Mỗi viên đá xuất hiện hai lần, ngoại trừ một viên đá duy nhất xuất hiện một lần.
#Nhiệm vụ của bạn là giúp Arithmos tìm viên đá xuất hiện lẻ lần.

#Input
#Dòng đầu tiên chứa số nguyên t — số lượng trường hợp kiểm tra.
#Mỗi trường hợp gồm:
#Dòng đầu tiên là số nguyên n — số lượng viên đá.
#Dòng thứ hai chứa n số nguyên a[i] — các số ghi trên viên đá.

#Output
#Với mỗi trường hợp, in ra số xuất hiện lẻ lần.


t = int(input())
for _ in range(t):
    n = int(input())
    da = list(map(int, input().split()))
    result = 0
    for number in da:
        result ^= number  
    print(result)  
