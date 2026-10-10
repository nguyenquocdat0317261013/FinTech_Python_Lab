 #Tinh_lai_suat_tiet_kiem
lai_suat_nam = 0.06

# Nhập số tiền gốc và thời gian gửi 
so_tien_goc = float(input("Nhập số tiền gốc (VNĐ): "))
thoi_gian = float(input("Nhập thời gian gửi (năm): "))

# Tính tổng số tiền theo công thức lãi đơn
tong_tien = so_tien_goc * (1 + lai_suat_nam * thoi_gian)

# Định dạng số tiền có dấu phẩy 
print(f"Tổng số tiền nhận được: {tong_tien:,.0f} VNĐ")
