 #phan_loai_khach_hang(diem_credit)
 # Nhập điểm từ bàn phím (dùng int() để đổi chữ thành số nguyên)
diem_credit = int(input("Nhập điểm tín dụng của khách hàng: "))
if diem_credit >= 750:
  print("Rủi ro Thấp - Duyệt tự động")
elif diem_credit >= 600:
  print("Rủi ro Trung bình - Cần thẩm định")
else:
  print("Rủi ro Cao - Từ chối cấp tín dụng")
