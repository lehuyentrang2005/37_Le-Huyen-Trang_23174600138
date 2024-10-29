class DaGiac:
    def __init__(self, ten):
        self.ten = ten
    def dien_tich(self):
        raise NotImplementedError("Phương thức này chưa được định nghĩa.")
    def chu_vi(self):
        raise NotImplementedError("Phương thức này chưa được định nghĩa.")
class HinhBinhHanh(DaGiac):
    def __init__(self, day, cao):
        super().__init__("Hình bình hành")
        self.day = day
        self.cao = cao
    def dien_tich(self):
        return self.day * self.cao
    def chu_vi(self):
        return 2 * (self.day + self.cao)
class HinhChuNhat(HinhBinhHanh):
    def __init__(self, dai, rong):
        super().__init__(dai, rong)
        self.dai = dai
        self.rong = rong
    def dien_tich(self):
        return self.dai * self.rong
    def chu_vi(self):
        return 2 * (self.dai + self.rong)
class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)
        self.canh = canh
def main():
    while True:
        loai_hinh = input("Nhập loại hình (hình bình hành, hình chữ nhật, hình vuông) hoặc 'exit' để thoát: ").strip().lower()
        if loai_hinh == 'exit':
            break
        if loai_hinh == 'hình bình hành':
            day = float(input("Nhập độ dài đáy: "))
            cao = float(input("Nhập chiều cao: "))
            hinh = HinhBinhHanh(day, cao)
        elif loai_hinh == 'hình chữ nhật':
            dai = float(input("Nhập chiều dài: "))
            rong = float(input("Nhập chiều rộng: "))
            hinh = HinhChuNhat(dai, rong)
        elif loai_hinh == 'hình vuông':
            canh = float(input("Nhập độ dài cạnh: "))
            hinh = HinhVuong(canh)
        else:
            print("Loại hình không hợp lệ. Vui lòng thử lại.")
            continue
        print(f"Diện tích của {hinh.ten}: {hinh.dien_tich()}")
        print(f"Chu vi của {hinh.ten}: {hinh.chu_vi()}")
        print("-" * 30)
if __name__ == "__main__":
    main()


