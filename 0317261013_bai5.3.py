V = 20.0
ty_gia = [-0.03, 0.0, 0.03]
lai_suat = [-0.02, -0.01, 0.01, 0.02]

print("=== MA TRẬN PHÂN TÍCH ĐỘ NHẠY GIÁ TRỊ DANH MỤC (TỶ VNĐ) ===")
print(f"Vốn danh mục ban đầu: {V:.2f} Tỷ VNĐ\n")
print(f"{'Lãi suất (Dòng) \\ Tỷ giá (Cột)':<32}| {'-3.0%':>9} | {'0.0%':>9} | {'+3.0%':>9}")
print("-" * 74)

for ir in lai_suat:                          # vòng ngoài: các dòng
    dong = f"{'Lãi suất: ' + f'{ir*100:+.1f}%':<32}"
    for ex in ty_gia:                        # vòng trong: các cột
        v_moi = V * (1 + 1.5*ex - 2.0*ir)
        dong += f"| {f'{v_moi:.2f} Tỷ':>9} "
    print(dong)
print("-" * 74)
