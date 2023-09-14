import tkinter as tk
from tkinter import messagebox
import time

# 创建主窗口
root = tk.Tk()
root.title("专注时钟")

# 设置倒计时的初始值（以秒为单位）
initial_time = 25 * 60  # 25分钟

# 创建倒计时变量
countdown_time = tk.StringVar()
countdown_time.set(time.strftime("%M:%S", time.gmtime(initial_time)))

# 倒计时函数
def countdown():
    global initial_time
    if initial_time > 0:
        initial_time -= 1
        countdown_time.set(time.strftime("%M:%S", time.gmtime(initial_time)))
        root.after(1000, countdown)  # 每隔1秒更新一次
    else:
        messagebox.showinfo("时间到", "专注时间已结束！")
        initial_time = 25 * 60
        countdown_time.set(time.strftime("%M:%S", time.gmtime(initial_time)))

# 开始计时按钮
start_button = tk.Button(root, text="开始计时", command=countdown)
start_button.pack()

# 停止计时按钮
stop_button = tk.Button(root, text="停止计时", command=root.quit)
stop_button.pack()

# 显示倒计时
label = tk.Label(root, textvariable=countdown_time, font=("Helvetica", 48))
label.pack()

root.mainloop()
