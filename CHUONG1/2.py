class TS:
    def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa):
        self.ho_ten=ho_ten
        self.diem_toan=diem_toan
        self.diem_ly=diem_ly
        self.diem_hoa=diem_hoa
    def tong_diem(self):
        return self.diem_toan+self.diem_ly+self.diem_hoa
    def in_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}, Tổng diểm: {self.tong_diem()}")
def nhap_thi_sinh():
    ho_ten=input("Nhập họ tên thí sinh")
    diem_toan=float(input("Điểm toán: "))
    diem_ly=float(input("Điểm lý: "))
    diem_hoa=floay(input("Điểm hóa: "))
    return TS(ho_ten, diem_toan, diem_ly, diem_hoa)
def main():
    danh_sach=[nhap_thi_sinh() for _ in range(int(input("Số lượng thí sinh")))] 
    trung_tuyen=[ts for ts in danh_sach if ts.tong_diem() >= 20]
    trung_tuyen.sort(key=lambda ts: ts.tong_diem(), reverse=True)
    print("\nDanh sách thí sinh trúng tuyển:")
    for ts in trun_tuyen:
        ts.in_thong_tin()
if __name__=="main":
    main()
    