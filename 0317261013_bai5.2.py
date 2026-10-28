F = 1_000_000.0      # Mệnh giá
c = 0.09             # Lãi suất coupon
N = 10               # Thời hạn (năm)
y = 0.085            # YTM

C = F * c
tong_pv_coupon = 0.0

print("=== ĐỊNH GIÁ TRÁI PHIẾU DOANH NGHIỆP ===")
print(f"Tiền lãi coupon hàng năm: {C:,.0f} VNĐ\n")
print(f"{'Năm':>4} | {'Coupon':>12} | {'PV coupon':>14}")
print("-" * 38)

for t in range(1, N + 1):
    pv_c = C / ((1 + y) ** t)
    tong_pv_coupon += pv_c
    print(f"{t:>4} | {C:>12,.0f} | {pv_c:>14,.0f}")

pv_f = F / ((1 + y) ** N)
gia_trai_phieu = tong_pv_coupon + pv_f

print("-" * 38)
print(f"Tổng PV coupon:        {tong_pv_coupon:>14,.0f} VNĐ")
print(f"PV mệnh giá (năm {N}):  {pv_f:>14,.0f} VNĐ")
print(f"Giá lý thuyết P0:      {gia_trai_phieu:>14,.0f} VNĐ")

if gia_trai_phieu > F:
    print("KẾT LUẬN: Trái phiếu bán CAO HƠN mệnh giá (Premium).")
elif gia_trai_phieu < F:
    print("KẾT LUẬN: Trái phiếu bán THẤP HƠN mệnh giá (Discount).")
else:
    print("KẾT LUẬN: Trái phiếu bán ĐÚNG mệnh giá (Par).")
