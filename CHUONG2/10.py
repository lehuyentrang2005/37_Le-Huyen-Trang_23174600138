import json
from collections import defaultdict
data = '''
{
    "cong_ty": {
        "ten": "Công ty TNHH Đất Việt",
        "dia_chi": "abc Giải Phóng - Hà Nội"
    },
    "nhan_vien": [
        {"ten": "Alice", "don_vi": "Đơn vị Al"},
        {"ten": "Bob", "don_vi": "Đơn vị A2"},
        {"ten": "Charlie", "don_vi": "Đơn vị Al"},
        {"ten": "David", "don_vi": "Đơn vị A3"},
        {"ten": "Eve", "don_vi": "Đơn vị A2"},
        {"ten": "Frank", "don_vi": "Đơn vị A4"},
        {"ten": "Grace", "don_vi": "Đơn vị A4"}
    ]
}
'''
du_lieu = json.loads(data)
thong_ke_don_vi = defaultdict(int)
for nhan_vien in du_lieu['nhan_vien']:
    thong_ke_don_vi[nhan_vien['don_vi']] += 1
tong_so_nhan_vien = len(du_lieu['nhan_vien'])
print(f"Tên công ty: {du_lieu['cong_ty']['ten']}")
print(f"Địa chỉ: {du_lieu['cong_ty']['dia_chi']}")
print("-_- Thống kê nhân viên theo đơn vị --")
for index, (don_vi, so_nhan_vien) in enumerate(thong_ke_don_vi.items(), start=1):
    ty_le = (so_nhan_vien / tong_so_nhan_vien) * 100
    print(f"{index}. /Tên đơn vị: {don_vi}.")
    print(f"- Số nhân viên: {so_nhan_vien}")
    print(f"- Tỷ lệ: {ty_le:.2f} %\n")

