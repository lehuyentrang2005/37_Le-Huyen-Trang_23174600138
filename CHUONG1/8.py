class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year
    def display(self):
        print(f"{self.day:02d}/{self.month:02d}/{self.year}")
    def next(self):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            days_in_month[1] = 29
        self.day += 1
        if self.day > days_in_month[self.month - 1]:
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1
class Employee:
    def __init__(self, name, birth_date, joining_date):
        self.name = name
        self.birth_date = birth_date  
        self.joining_date = joining_date  
    def display_info(self):
        print(f"Họ tên: {self.name}")
        print("Ngày sinh: ", end="")
        self.birth_date.display()
        print("Ngày vào công ty: ", end="")
        self.joining_date.display()
def main():
    employees = []
    while True:
        name = input("Nhập họ tên nhân viên (hoặc 'exit' để thoát): ")
        if name.lower() == 'exit':
            break
        day_birth = int(input("Nhập ngày sinh: "))
        month_birth = int(input("Nhập tháng sinh: "))
        year_birth = int(input("Nhập năm sinh: "))
        birth_date = Date(day_birth, month_birth, year_birth)
        day_join = int(input("Nhập ngày vào công ty: "))
        month_join = int(input("Nhập tháng vào công ty: "))
        year_join = int(input("Nhập năm vào công ty: "))
        joining_date = Date(day_join, month_join, year_join)
        employee = Employee(name, birth_date, joining_date)
        employees.append(employee)
    print("\nDanh sách nhân viên:")
    for emp in employees:
        emp.display_info()
        print("-" * 30)
if __name__ == "__main__":
    main()
