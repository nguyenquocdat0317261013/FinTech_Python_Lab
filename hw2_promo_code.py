# hw2_promo_code

# Nhập thông tin
ho_ten = input("Nhập họ tên: ").strip()
nam_sinh = input("Nhập năm sinh: ").strip()

# Lấy tên (từ cuối cùng trong họ tên)
ten = ho_ten.split()[-1]

# Lấy tối đa 3 ký tự đầu của tên và viết hoa
ten_3_ky_tu = ten[0:3].upper()

# Ghép thành mã ưu đãi và in ra
ma_uu_dai = ten_3_ky_tu + "-" + nam_sinh + "-VIP"
print("Mã ưu đãi:", ma_uu_dai)
