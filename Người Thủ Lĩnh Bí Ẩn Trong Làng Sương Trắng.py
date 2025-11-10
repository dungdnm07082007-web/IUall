#Tại làng Sương Trắng, mỗi năm dân làng sẽ tổ chức Lễ Hội Bình Chọn Thủ Lĩnh. Nơi đây sống nhiều gia tộc, mỗi gia tộc đại diện bởi một ký hiệu riêng (ký hiệu được biểu diễn bằng một chuỗi ký tự).
#Trong lễ hội, mỗi người dân sẽ bỏ phiếu (ký hiệu gia tộc mà họ muốn), và gia tộc nào nhận được nhiều phiếu nhất sẽ trở thành Thủ Lĩnh Làng.
#Tuy nhiên, có một quy tắc cổ xưa:
#“Một gia tộc chỉ được công nhận làm Thủ Lĩnh khi số phiếu của họ nhiều hơn một nửa tổng số phiếu.”
#Nếu không có gia tộc nào đạt điều kiện đó, làng sẽ không có thủ lĩnh trong năm đó.
#Nhiệm vụ của bạn là giúp Eira – người ghi chép lễ hội – xác định gia tộc chiến thắng, hoặc thông báo "NO" nếu không có ai đạt điều kiện.

#Nhiệm vụ
#Có t lần tổ chức lễ hội.
#Với mỗi lần:
#Nhập vào số dân tham gia n.
#Nhập danh sách n ký hiệu phiếu bầu.
#Xác định xem có ký hiệu nào xuất hiện hơn n/2 lần hay không.
#Nếu có, in ký hiệu đó.
#Nếu không, in "NO".

#Dữ liệu vào
#Dòng 1: Số nguyên t — số lần tổ chức lễ hội.
#Với mỗi lần:
#Dòng 1: Số nguyên n
#Dòng 2: n chuỗi ký hiệu (các ký hiệu có thể lặp lại)

#Dữ liệu ra
#Với mỗi lần, in ra ký hiệu của gia tộc thắng hoặc "NO" nếu không có ai đủ điều kiện.

#Ràng buộc
#1 ≤ t ≤ 100
#1 ≤ n ≤ 10^5
#Tổng số phần tử trong tất cả test không vượt quá 10^6
#Mỗi ký hiệu là chuỗi không rỗng, không chứa khoảng trắng.


t = int(input())
for _ in range(t):
    n = int(input())
    phieu_bau_list = input().split()
    dem_phieu = {}
    for phieu in phieu_bau_list:
        dem_phieu[phieu] = dem_phieu.get(phieu, 0) + 1
        nguong_thanh_lap_thu_linh = n / 2
        thu_linh = "NO"
        for ky_hieu_gia_toc, so_lan_dem in dem_phieu.items():
            if so_lan_dem > nguong_thanh_lap_thu_linh:
                thu_linh = ky_hieu_gia_toc
                break
    print(thu_linh)