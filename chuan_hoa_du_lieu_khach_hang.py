 #chuan_hoa_du_lieu_khach_hang 
# Tên khách hàng ban đầu (chưa chuẩn hóa)
ten_khach_hang = input("Nhập tên khách hàng cần chuẩn hóa: ")

# Chuẩn hóa: Xóa khoảng trắng thừa và viết hoa chữ cái đầu mỗi từ
ten_chuan_hoa = ten_khach_hang.strip().title()

# In kết quả ra màn hình
print("Tên sau khi chuẩn hóa:", ten_chuan_hoa)
