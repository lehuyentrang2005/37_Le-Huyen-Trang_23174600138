class Stack:
    def __init__(self, size):
        self.size=size
        self.stack=[]
    def push(self, item):
        if self.isFull():
            print("Ngăn xếp đã đầy, không thể thêm phần tử")
        else:
            self.stack.append(item)
            print(f"Đã thêm phần tử: {item}")
    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp trống, không thể lấy phần tử")
            return None
        else:
            item=self.stack.pop()
            print(f"Đã lấy phần tử: {item}")
            return item
    def isEmpty(self):
        return len(self.stack)==0
    def isFull(self):
        return len(self.stack) >= self.size
    def count(self):
        return len(self.stack)
def main():
    size=int(input("Nhập kích thước ngăn xếp: "))
    stack=Stack(size)

    while True:
        action=input("Nhập 'push' để thêm, 'pop' để lấy, 'count' để đếm, 'exit' để thoát: ").strip().lower()
        if action=='push':
            item=float(input("Nhập phần tử (float): "))
            stack.push(item)
        elif action == 'pop':
            stack.pop()
        elif action=='count':
            print(f"Số phần tử trên ngăn xếp: {stack.count()}")
        elif action=='exit':
            break
        else:
            print("Lựa chọn không hợp lệ")
if __name__=="__main__":
    main()



