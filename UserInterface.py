import tkinter as tk
from tkinter import filedialog

def start_bot():
    excel_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    print("فایل انتخاب شد:", excel_path)
    # اینجا میتونی کد رباتت رو صدا بزنی

root = tk.Tk()
root.title("ربات ثبت VAT169")
root.geometry("300x150")

btn = tk.Button(root, text="انتخاب فایل اکسل و شروع", command=start_bot)
btn.pack(pady=40)

root.mainloop()
