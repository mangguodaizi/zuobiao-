import tkinter as tk
from tkinter import messagebox

# 打印Python版本信息
import sys
print(f"Python版本: {sys.version}")
print(f"Tkinter版本: {tk.Tcl().eval('info patchlevel')}")

# 创建一个简单的Tkinter窗口
root = tk.Tk()
root.title("测试窗口")
root.geometry("300x200")

# 添加标签
label = tk.Label(root, text="坐标工具测试", font=("SimHei", 14))
label.pack(pady=20)

# 添加按钮
def show_message():
    messagebox.showinfo("成功", "Tkinter正常工作！")
    root.destroy()

button = tk.Button(root, text="点击测试", command=show_message, font=("SimHei", 12))
button.pack(pady=20)

print("窗口已创建，点击按钮测试消息框...")

# 运行主循环
root.mainloop()

print("测试完成！")