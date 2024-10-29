import json
from datetime import datetime
giao_dich = []
def them_giao_dich():
    loai_giao_dich = input("Nhập loại giao dịch (tiền/vàng): ")
    so_tien = float(input("Nhập số tiền (hoặc số vàng): "))
    giao_dich.append({"loai": loai_giao_dich, "so": so_tien})
while True:
    them_giao_dich()
    tiep_tuc = input("Bạn có muốn thêm giao dịch nữa không? (1: Có, 0: Không): ")
    if tiep_tuc == '0':
        break
ghi_vao_tap_tin = input("Bạn có muốn ghi vào tệp không? (1: Có, 0: Không): ")
if ghi_vao_tap_tin == '1':
    thoi_gian_hien_tai = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    ten_tap_tin = f"{thoi_gian_hien_tai}.json"
    with open(ten_tap_tin, 'w', encoding='utf-8') as f:
        json.dump(giao_dich, f, ensure_ascii=False, indent=4)
    print(f"Dữ liệu đã được ghi vào tệp: {ten_tap_tin}")
else:
    print("Không ghi dữ liệu vào tệp.")
