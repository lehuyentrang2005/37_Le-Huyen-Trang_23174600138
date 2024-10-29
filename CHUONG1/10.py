import math
class Diem:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
class Elip(Diem):
    def __init__(self, x, y, banKinhLon, banKinhNho):
        super().__init__(x, y)
        self.banKinhLon = banKinhLon
        self.banKinhNho = banKinhNho
    def dienTich(self):
        return math.pi * self.banKinhLon * self.banKinhNho
class DuongTron(Elip):
    def __init__(self, x, y, banKinh):
        super().__init__(x, y, banKinh, banKinh)
def main():
    print("Nhập thông tin cho elip:")
    x = float(input("Nhập hoành độ (x): "))
    y = float(input("Nhập tung độ (y): "))
    banKinhLon = float(input("Nhập bán kính lớn: "))
    banKinhNho = float(input("Nhập bán kính nhỏ: "))
    elip = Elip(x, y, banKinhLon, banKinhNho)
    print(f"Diện tích của elip: {elip.dienTich()}")
    print("\nNhập thông tin cho đường tròn:")
    banKinh = float(input("Nhập bán kính: "))
    duong_tron = DuongTron(x, y, banKinh)
    print(f"Diện tích của đường tròn: {duong_tron.dienTich()}")
if __name__ == "__main__":
    main()
