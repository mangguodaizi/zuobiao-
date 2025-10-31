import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

class CoordinateTool:
    def __init__(self, root):
        self.root = root
        self.root.title("坐标位置计算工具")
        self.root.geometry("600x450")
        self.root.resizable(True, True)
        
        # 设置中文字体
        self.style = ttk.Style()
        self.style.configure(
            "TLabel", 
            font=("SimHei", 10),
            padding=5
        )
        self.style.configure(
            "TButton", 
            font=("SimHei", 10),
            padding=5
        )
        self.style.configure(
            "TEntry", 
            font=("SimHei", 10),
            padding=5
        )
        
        # 字体引用，用于需要直接设置字体的地方
        self.font = ("SimHei", 10)
        
        # 坐标数据
        self.current_x = tk.StringVar(value="0")
        self.current_y = tk.StringVar(value="0")
        self.coordinates_list = []
        self.saved_coordinates = {}
        
        # 创建主框架
        self.main_frame = ttk.Frame(root, padding=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 创建UI组件
        self.create_widgets()
        
        # 加载已保存的坐标
        self.load_saved_coordinates()
        
        # 绑定快捷键
        self.bind_shortcuts()
    
    def create_widgets(self):
        # 当前坐标显示
        ttk.Label(self.main_frame, text="当前坐标:", font=("SimHei", 12)).grid(row=0, column=0, sticky=tk.W, pady=5)
        
        coordinate_frame = ttk.Frame(self.main_frame)
        coordinate_frame.grid(row=1, column=0, sticky=tk.W, pady=5)
        
        ttk.Label(coordinate_frame, text="X: ").grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(coordinate_frame, textvariable=self.current_x, width=10).grid(row=0, column=1, padx=5)
        
        ttk.Label(coordinate_frame, text="Y: ").grid(row=0, column=2, sticky=tk.W, padx=(20, 0))
        ttk.Entry(coordinate_frame, textvariable=self.current_y, width=10).grid(row=0, column=3, padx=5)
        
        # 按钮区域
        button_frame = ttk.Frame(self.main_frame)
        button_frame.grid(row=2, column=0, sticky=tk.W, pady=10)
        
        ttk.Button(button_frame, text="获取当前鼠标位置", command=self.get_mouse_position).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="添加到列表", command=self.add_coordinate).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="清除列表", command=self.clear_list).pack(side=tk.LEFT, padx=5)
        
        # 坐标名称输入
        name_frame = ttk.Frame(self.main_frame)
        name_frame.grid(row=3, column=0, sticky=tk.W, pady=5)
        
        ttk.Label(name_frame, text="坐标名称: ").grid(row=0, column=0, sticky=tk.W)
        self.coord_name = ttk.Entry(name_frame, width=20)
        self.coord_name.grid(row=0, column=1, padx=5)
        
        # 保存区域
        save_frame = ttk.Frame(self.main_frame)
        save_frame.grid(row=4, column=0, sticky=tk.W, pady=5)
        
        ttk.Button(save_frame, text="保存当前坐标", command=self.save_coordinate).pack(side=tk.LEFT, padx=5)
        ttk.Button(save_frame, text="显示所有保存的坐标", command=self.show_saved_coordinates).pack(side=tk.LEFT, padx=5)
        
        # 坐标列表显示
        ttk.Label(self.main_frame, text="坐标列表:", font=("SimHei", 12)).grid(row=5, column=0, sticky=tk.W, pady=5)
        
        self.list_frame = ttk.Frame(self.main_frame)
        self.list_frame.grid(row=6, column=0, sticky=tk.NSEW, pady=5)
        
        # 创建滚动条
        scrollbar = ttk.Scrollbar(self.list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.coordinates_text = tk.Text(self.list_frame, height=10, width=50, yscrollcommand=scrollbar.set, font=self.font)
        self.coordinates_text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.coordinates_text.yview)
        
        # 坐标计算区域
        ttk.Label(self.main_frame, text="坐标计算:", font=("SimHei", 12)).grid(row=7, column=0, sticky=tk.W, pady=5)
        
        calc_frame = ttk.Frame(self.main_frame)
        calc_frame.grid(row=8, column=0, sticky=tk.W, pady=5)
        
        ttk.Button(calc_frame, text="计算两点距离", command=self.calculate_distance).pack(side=tk.LEFT, padx=5)
        ttk.Button(calc_frame, text="计算中点坐标", command=self.calculate_midpoint).pack(side=tk.LEFT, padx=5)
        
        # 结果显示
        self.result_var = tk.StringVar(value="计算结果将显示在这里")
        ttk.Label(self.main_frame, textvariable=self.result_var, font=self.font).grid(row=9, column=0, sticky=tk.W, pady=5)
        
        # 底部提示和作者信息
        ttk.Label(self.main_frame, text="快捷键: F1-获取坐标 | F2-添加到列表 | F3-保存坐标 | ESC-退出 | 作者：怪气养胃多", font=('SimHei', 8, 'italic')).grid(row=10, column=0, sticky=tk.SE, pady=10)
        
        # 配置网格权重，使界面可拉伸
        self.main_frame.columnconfigure(0, weight=1)
        for i in range(11):
            self.main_frame.rowconfigure(i, weight=0)
        self.main_frame.rowconfigure(6, weight=1)
    
    def get_mouse_position(self):
        """获取当前鼠标位置"""
        try:
            # 使用Tkinter的方法获取鼠标位置（相对于屏幕）
            root_x = self.root.winfo_pointerx()
            root_y = self.root.winfo_pointery()
            self.current_x.set(str(root_x))
            self.current_y.set(str(root_y))
            self.result_var.set(f"已获取鼠标位置: ({root_x}, {root_y})")
            # 显示提示
            self.show_tooltip("已获取鼠标位置")
        except Exception as e:
            messagebox.showerror("错误", f"获取鼠标位置失败: {str(e)}")
    
    def add_coordinate(self):
        """添加当前坐标到列表"""
        try:
            x = int(self.current_x.get())
            y = int(self.current_y.get())
            name = self.coord_name.get() or f"点{len(self.coordinates_list) + 1}"
            
            coord = (x, y, name)
            self.coordinates_list.append(coord)
            
            # 更新文本框
            self.coordinates_text.insert(tk.END, f"{name}: ({x}, {y})\n")
            self.coordinates_text.see(tk.END)
            
            self.result_var.set(f"已添加坐标: {name} ({x}, {y})")
            self.coord_name.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("错误", "请输入有效的坐标值")
    
    def save_coordinate(self):
        """保存当前坐标"""
        try:
            x = int(self.current_x.get())
            y = int(self.current_y.get())
            name = self.coord_name.get()
            
            if not name:
                messagebox.showerror("错误", "请输入坐标名称")
                return
            
            self.saved_coordinates[name] = (x, y)
            self.save_to_file()
            
            self.result_var.set(f"已保存坐标: {name} ({x}, {y})")
            self.coord_name.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("错误", "请输入有效的坐标值")
    
    def save_to_file(self):
        """保存坐标到文件"""
        try:
            with open("saved_coordinates.json", "w", encoding="utf-8") as f:
                json.dump(self.saved_coordinates, f, ensure_ascii=False, indent=2)
        except Exception as e:
            messagebox.showerror("保存错误", f"无法保存坐标: {str(e)}")
    
    def clear_list(self):
        """清除坐标列表"""
        self.coordinates_list.clear()
        self.coordinates_text.delete(1.0, tk.END)
        self.result_var.set("坐标列表已清除")
    
    def load_saved_coordinates(self):
        """从文件加载坐标"""
        try:
            if os.path.exists("saved_coordinates.json"):
                with open("saved_coordinates.json", "r", encoding="utf-8") as f:
                    self.saved_coordinates = json.load(f)
        except Exception as e:
            messagebox.showerror("加载错误", f"无法加载保存的坐标: {str(e)}")
    
    def show_saved_coordinates(self):
        """显示所有保存的坐标"""
        if not self.saved_coordinates:
            messagebox.showinfo("信息", "没有保存的坐标")
            return
        
        # 创建新窗口显示保存的坐标
        save_window = tk.Toplevel(self.root)
        save_window.title("保存的坐标")
        save_window.geometry("400x300")
        
        # 创建滚动条和文本框
        scrollbar = ttk.Scrollbar(save_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        text_widget = tk.Text(save_window, yscrollcommand=scrollbar.set, font=self.font)
        text_widget.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=text_widget.yview)
        
        # 添加坐标信息
        for name, (x, y) in self.saved_coordinates.items():
            text_widget.insert(tk.END, f"{name}: ({x}, {y})\n")
        
        # 添加复制到剪贴板功能
        def copy_to_clipboard():
            code = "# 保存的坐标\n"
            for name, (x, y) in self.saved_coordinates.items():
                code += f"{name} = ({x}, {y})\n"
            
            self.root.clipboard_clear()
            self.root.clipboard_append(code)
            messagebox.showinfo("成功", "坐标代码已复制到剪贴板")
        
        ttk.Button(save_window, text="复制为Python代码", command=copy_to_clipboard).pack(pady=10)
    
    def calculate_distance(self):
        """计算两点距离"""
        if len(self.coordinates_list) < 2:
            messagebox.showerror("错误", "请至少添加两个坐标点")
            return
        
        try:
            # 使用最后两个点计算距离
            x1, y1, _ = self.coordinates_list[-2]
            x2, y2, _ = self.coordinates_list[-1]
            
            distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            self.result_var.set(f"两点之间距离: {distance:.2f}")
        except Exception as e:
            messagebox.showerror("计算错误", str(e))
    
    def calculate_midpoint(self):
        """计算中点坐标"""
        if len(self.coordinates_list) < 2:
            messagebox.showerror("错误", "请至少添加两个坐标点")
            return
        
        try:
            # 使用最后两个点计算中点
            x1, y1, _ = self.coordinates_list[-2]
            x2, y2, _ = self.coordinates_list[-1]
            
            mid_x = (x1 + x2) // 2
            mid_y = (y1 + y2) // 2
            
            self.result_var.set(f"中点坐标: ({mid_x}, {mid_y})")
            # 自动添加中点到列表
            self.current_x.set(str(mid_x))
            self.current_y.set(str(mid_y))
        except Exception as e:
            messagebox.showerror("计算错误", str(e))
    
    def bind_shortcuts(self):
        """绑定快捷键"""
        # 退出程序
        self.root.bind("<Escape>", lambda event: self.exit_app())
        
        # 获取当前鼠标位置（F1键）
        self.root.bind("<F1>", lambda event: self.get_mouse_position())
        
        # 添加当前坐标到列表（F2键）
        self.root.bind("<F2>", lambda event: self.add_coordinate())
        
        # 保存当前坐标（F3键）
        self.root.bind("<F3>", lambda event: self.save_coordinate())
        
        # 确保窗口可以接收焦点以响应快捷键
        self.root.focus_force()
    
    def show_tooltip(self, message):
        """显示临时提示信息"""
        tooltip = tk.Toplevel(self.root)
        tooltip.wm_overrideredirect(True)  # 无边框窗口
        
        # 计算位置：在主窗口上方居中显示
        x = self.root.winfo_x() + (self.root.winfo_width() // 2)
        y = self.root.winfo_y() - 30
        
        tooltip.geometry(f"+{x - 75}+{y}")  # 调整位置使提示框居中
        
        # 创建提示标签
        label = tk.Label(tooltip, text=message, bg="black", fg="white", 
                        font=self.font, padx=10, pady=5)
        label.pack()
        
        # 2秒后自动关闭提示
        tooltip.after(2000, tooltip.destroy)
    
    def exit_app(self):
        """退出应用程序"""
        if messagebox.askyesno("确认退出", "确定要退出吗？"):
            self.root.destroy()

if __name__ == "__main__":
    # 创建主窗口
    root = tk.Tk()
    
    # 创建应用实例
    app = CoordinateTool(root)
    root.mainloop()