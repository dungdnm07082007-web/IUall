#Trong vương quốc Lexiconia, mỗi câu chữ đều mang sức mạnh kỳ diệu. Tuy nhiên, nhiều cuộn sách cổ bị viết lộn xộn: chữ hoa chữ thường xen lẫn, khoảng trắng lung tung, dấu phẩy và dấu hai chấm xuất hiện tùy ý, thậm chí có những ký tự kỳ lạ không thuộc ngôn ngữ.
#Nhân vật chính:
#Liora, cô học giả trẻ đầy tò mò và thông minh, được giao nhiệm vụ chuẩn hóa các cuộn sách thần kỳ.

#Nhiệm vụ của Liora:
#Tách các từ dựa trên khoảng trắng, dấu phẩy , và dấu hai chấm : từ văn bản hỗn loạn.
#Biến chữ cái đầu của mỗi từ thành chữ hoa, các chữ cái còn lại thành chữ thường.
#Loại bỏ mọi ký tự không hợp lệ (ngoài chữ cái, chữ số, khoảng trắng, dấu phẩy và dấu hai chấm).
#Sự chính xác trong công việc của Liora quyết định việc các pháp sư có thể đọc được những bí mật cổ xưa hay không.

#Input
#Mỗi chuỗi kí tự có thể chứa chữ cái, chữ số, khoảng trắng, dấu phẩy ,, dấu hai chấm : hoặc các ký tự đặc biệt khác.

#Output
#Một chuỗi được chuẩn hóa theo quy tắc:
#Chữ cái đầu tiên mỗi từ viết hoa.
#Các chữ cái còn lại viết thường.
#Giữ nguyên khoảng trắng, dấu phẩy và dấu hai chấm.
#Loại bỏ các ký tự khác.


chuoi = input()
van_ban = ''
for c in chuoi:
    if c.isalnum() or c in ' ,:':
        van_ban += c
    else:
        van_ban += ' '
van_ban = ' '.join(van_ban.split())
ket_qua = ''
tu = ''
for c in van_ban:
    if c.isalnum():
        tu += c
    else:
        if tu:
            ket_qua += tu.capitalize()
            tu = ''
        ket_qua += c
if tu:
    ket_qua += tu.capitalize()
print(ket_qua)
