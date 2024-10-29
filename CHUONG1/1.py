class HinhChuNhat:
    def __init__(self, dai, rong):

        self.dai=dai
        self.rong=rong
    def tinh_chu_vi(self):
        return 2*(self.dai+self.rong)
    def tinh_dien_tich(self):
        return self.dai*self.rong
    def in_thong_tin(self):
        print(f"Độ dài chiều dài: {self.dai}")
        print(f"Độ dài chiều rộng: {self.rong}")
        print(f"Chu vi: {self.tinh_chu_vi()}")
        print(f"Diện tích: {self.tinh_dien_tich()}")

dai=float(input("Nhập độ dài chiều dài: "))
rong=float(input("Nhập độ dài chiều rộng: "))
hcn=HinhChuNhat(dai, rong)
hcn.in_thong_tin()