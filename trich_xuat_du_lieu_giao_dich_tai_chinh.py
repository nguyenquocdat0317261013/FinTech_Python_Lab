 #trich_xuat_du_lieu_giao_dich_tai_chinh
ma_giao_dich = "GD001-5000000-VND"

# Tách chuỗi dựa vào dấu '-' 
# Sau đó ép kiểu trực tiếp sang số nguyên (int)
so_tien = int(ma_giao_dich.split("-")[1])

# Kiểm tra điều kiện giao dịch
if so_tien >= 5000000:
  print("Giao dịch cần xác thực OTP")
else:
  print("Giao dịch thành công")
