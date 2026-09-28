# hw1_billsplit.py

# Nhập dữ liệu 
X = float(input("Nhập tổng hóa đơn: "))
Y = float(input("Nhập phần trăm tip (%): "))
N = int(input("Nhập số người chia: "))

# Tính tổng tiền bao gồm cả tiền tip
tong_tien = X + (X * Y / 100)

# Tính tiền mỗi người phải trả
tien_moi_nguoi = tong_tien / N

# Làm tròn đến số nguyên
tien_lam_tron = round(tien_moi_nguoi)

# In kết quả ra màn hình
print("Số tiền mỗi người phải trả là:", tien_lam_tron, "đồng")
