# hw1_email_masking

# Nhập email từ bàn phím
email = input("Nhập địa chỉ email của bạn: ")

#  Tách email thành phần tên và phần tên miền tại ký tự @
parts = email.split("@")
username = parts[0]
domain = parts[1]

# Lấy 3 ký tự đầu tiên của tên đăng nhập 
ten_3_ky_tu = username[0:3]

# Ghép chuỗi và in kết quả 
email_bi_che = ten_3_ky_tu + "***@" + domain
print("Kết quả:", email_bi_che)
