import math
class TamGiac:
    def __init__(self, a, b, c):
        self.a = a  # Cạnh a
        self.b = b  # Cạnh b
        self.c = c  # Cạnh c
    def dien_tich(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
class TamGiacVuong(TamGiac):
    def __init__(self, canh1, canh2):
        super().__init__(canh1, canh2, math.sqrt(canh1**2 + canh2**2))
    def dien_tich(self):
        return 0.5 * self.a * self.b
class TamGiacCan(TamGiac):
    def __init__(self, canhKe, canhChinh):
        super().__init__(canhKe, canhKe, canhChinh)
    def dien_tich(self):
        return (self.a * math.sqrt(self.b**2 - (self.a / 2)**2)) / 2
class TamGiacDeu(TamGiacCan):
    def __init__(self, canh):
        super().__init__(canh, canh)
    def dien_tich(self):
        return (math.sqrt(3) / 4) * (self.a ** 2)
def main():
    print("Nhập thông tin cho tam giác:")
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    tam_giac = TamGiac(a, b, c)
    print(f"Diện tích tam giác: {tam_giac.dien_tich()}")
    print("\nNhập thông tin cho tam giác vuông:")
    canh1 = float(input("Nhập cạnh góc vuông thứ nhất: "))
    canh2 = float(input("Nhập cạnh góc vuông thứ hai: "))
    tam_giac_vuong = TamGiacVuong(canh1, canh2)
    print(f"Diện tích tam giác vuông: {tam_giac_vuong.dien_tich()}")
    print("\nNhập thông tin cho tam giác cân:")
    canhKe = float(input("Nhập cạnh bên: "))
    canhChinh = float(input("Nhập cạnh đáy: "))
    tam_giac_can = TamGiacCan(canhKe, canhChinh)
    print(f"Diện tích tam giác cân: {tam_giac_can.dien_tich()}")
    print("\nNhập thông tin cho tam giác đều:")
    canh = float(input("Nhập cạnh: "))
    tam_giac_deu = TamGiacDeu(canh)
    print(f"Diện tích tam giác đều: {tam_giac_deu.dien_tich()}")
if __name__ == "__main__":
    main()
