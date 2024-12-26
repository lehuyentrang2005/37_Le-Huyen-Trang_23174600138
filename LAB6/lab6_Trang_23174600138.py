import sqlite3
import tkinter as tk
from tkinter import messagebox
conn = sqlite3.connect('product.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS product (
    Id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Price REAL NOT NULL,
    Amount INTEGER NOT NULL
)
''')
conn.commit()
def hien_thi_danh_sach():
    listbox.delete(0, tk.END)
    c.execute("SELECT * FROM product")
    products = c.fetchall()
    for product in products:
        listbox.insert(tk.END, f"ID: {product[0]}, Tên: {product[1]}, Giá: {product[2]}, Số lượng: {product[3]}")
def them_san_pham():
    name = entry_name.get()
    price = entry_price.get()
    amount = entry_amount.get()
    if name and price and amount:
        try:
            c.execute("INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)", (name, float(price), int(amount)))
            conn.commit()
            messagebox.showinfo("Thành công", "Đã thêm sản phẩm thành công!")
            hien_thi_danh_sach()
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")
def tim_kiem_san_pham():
    keyword = entry_search.get()
    listbox.delete(0, tk.END)
    c.execute("SELECT * FROM product WHERE Name LIKE ?", (f"%{keyword}%",))
    products = c.fetchall()
    if products:
        for product in products:
            listbox.insert(tk.END, f"ID: {product[0]}, Tên: {product[1]}, Giá: {product[2]}, Số lượng: {product[3]}")
    else:
        messagebox.showinfo("Thông báo", "Không tìm thấy sản phẩm nào.")
def cap_nhat_san_pham():
    try:
        product_id = int(entry_id.get())
        new_price = float(entry_price.get())
        new_amount = int(entry_amount.get())
        c.execute("UPDATE product SET Price = ?, Amount = ? WHERE Id = ?", (new_price, new_amount, product_id))
        conn.commit()
        messagebox.showinfo("Thành công", "Cập nhật sản phẩm thành công!")
        hien_thi_danh_sach()
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))
def xoa_san_pham():
    try:
        product_id = int(entry_id.get())
        c.execute("DELETE FROM product WHERE Id = ?", (product_id,))
        conn.commit()
        messagebox.showinfo("Thành công", "Xóa sản phẩm thành công!")
        hien_thi_danh_sach()
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))
root = tk.Tk()
root.title("Quản Lý Sản Phẩm")
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

lbl_name = tk.Label(frame_input, text="Tên sản phẩm:")
lbl_name.grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame_input)
entry_name.grid(row=0, column=1, padx=5, pady=5)

lbl_price = tk.Label(frame_input, text="Giá:")
lbl_price.grid(row=1, column=0, padx=5, pady=5)
entry_price = tk.Entry(frame_input)
entry_price.grid(row=1, column=1, padx=5, pady=5)

lbl_amount = tk.Label(frame_input, text="Số lượng:")
lbl_amount.grid(row=2, column=0, padx=5, pady=5)
entry_amount = tk.Entry(frame_input)
entry_amount.grid(row=2, column=1, padx=5, pady=5)

lbl_id = tk.Label(frame_input, text="ID sản phẩm:")
lbl_id.grid(row=3, column=0, padx=5, pady=5)
entry_id = tk.Entry(frame_input)
entry_id.grid(row=3, column=1, padx=5, pady=5)

btn_add = tk.Button(root, text="Thêm Sản Phẩm", command=them_san_pham)
btn_add.pack(pady=5)

btn_update = tk.Button(root, text="Cập Nhật Sản Phẩm", command=cap_nhat_san_pham)
btn_update.pack(pady=5)

btn_delete = tk.Button(root, text="Xóa Sản Phẩm", command=xoa_san_pham)
btn_delete.pack(pady=5)

frame_search = tk.Frame(root)
frame_search.pack(pady=10)

lbl_search = tk.Label(frame_search, text="Tìm kiếm:")
lbl_search.grid(row=0, column=0, padx=5, pady=5)
entry_search = tk.Entry(frame_search)
entry_search.grid(row=0, column=1, padx=5, pady=5)
btn_search = tk.Button(frame_search, text="Tìm", command=tim_kiem_san_pham)
btn_search.grid(row=0, column=2, padx=5, pady=5)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

btn_show = tk.Button(root, text="Hiển Thị Danh Sách", command=hien_thi_danh_sach)
btn_show.pack(pady=5)
hien_thi_danh_sach()
root.mainloop()
conn.close()
