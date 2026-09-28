# hw2_roi.py 

# Nhập dữ liệu 
tong_von = float(input("Nhập tổng vốn ban đầu: "))
gia_tri_ban = float(input("Nhập tổng giá trị bán ra: "))

# Tính lợi nhuận ròng
loi_nhuan_rong = gia_tri_ban - tong_von

# Tính tỷ lệ ROI (%)
roi = (loi_nhuan_rong / tong_von) * 100

# In kết quả trực tiếp ra màn hình
print("Lợi nhuận ròng:", loi_nhuan_rong)
print("Tỷ suất sinh lời (ROI):", roi, "%")
