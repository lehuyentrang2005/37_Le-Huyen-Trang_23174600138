class PS:
    def __init__(self, tu_so=0, mau_so=1):
        self.tu_so = tu_so
        self.mau_so = mau_so

    def kiem_tra_hop_le(self):
        return self.mau_so != 0

    def nhap_phan_so(self):
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))
        if not self.kiem_tra_hop_le():
            print("Mẫu số không hợp lệ (không được bằng 0).")

    def in_phan_so(self):
        if self.kiem_tra_hop_le():
            print(f"Phân số: {self.tu_so}/{self.mau_so}")
        else:
            print("Phân số không hợp lệ.")

def main():
    ps = PS()
    ps.nhap_phan_so()
    ps.in_phan_so()

if __name__ == "__main__":
    main()
