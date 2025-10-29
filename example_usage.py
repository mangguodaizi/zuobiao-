#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
坐标工具使用示例

这个文件展示了如何在实际项目中使用坐标工具保存的坐标数据
"""

import json
import os
import time

# 方法1: 直接使用硬编码的坐标
# 从坐标工具复制的坐标代码
# 注意：这里只是示例，实际使用时请替换为您从工具中复制的真实坐标
def use_hardcoded_coordinates():
    """使用硬编码的坐标数据"""
    print("方法1: 使用硬编码的坐标")
    
    # 从坐标工具复制的坐标代码示例
    login_button = (500, 300)
    username_field = (400, 250)
    password_field = (400, 280)
    submit_button = (550, 350)
    
    # 打印坐标信息
    print(f"登录按钮坐标: {login_button}")
    print(f"用户名输入框坐标: {username_field}")
    print(f"密码输入框坐标: {password_field}")
    print(f"提交按钮坐标: {submit_button}")
    
    # 模拟使用坐标执行操作
    print("\n模拟执行操作:")
    print(f"1. 移动鼠标到用户名输入框: {username_field}")
    print(f"2. 点击输入框")
    print(f"3. 输入用户名")
    print(f"4. 移动鼠标到密码输入框: {password_field}")
    print(f"5. 点击输入框")
    print(f"6. 输入密码")
    print(f"7. 移动鼠标到登录按钮: {login_button}")
    print(f"8. 点击登录按钮")
    print()

# 方法2: 从JSON文件加载坐标
def load_coordinates_from_json(file_path="saved_coordinates.json"):
    """从JSON文件加载保存的坐标"""
    print("方法2: 从JSON文件加载坐标")
    
    if not os.path.exists(file_path):
        print(f"错误: 找不到坐标文件 {file_path}")
        print("请先使用坐标工具保存坐标数据")
        return None
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            coordinates = json.load(f)
        
        print(f"成功从 {file_path} 加载坐标数据")
        print(f"共加载 {len(coordinates)} 个坐标点:")
        
        for name, (x, y) in coordinates.items():
            print(f"- {name}: ({x}, {y})")
        
        return coordinates
    except Exception as e:
        print(f"加载坐标文件时出错: {str(e)}")
        return None

# 方法3: 创建一个坐标管理类
def use_coordinate_manager():
    """使用坐标管理类"""
    print("\n方法3: 使用坐标管理类")
    
    class CoordinateManager:
        def __init__(self, file_path="saved_coordinates.json"):
            self.file_path = file_path
            self.coordinates = self._load_coordinates()
        
        def _load_coordinates(self):
            """加载坐标数据"""
            if not os.path.exists(self.file_path):
                return {}
            
            try:
                with open(self.file_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return {}
        
        def get_coordinate(self, name, default=None):
            """获取指定名称的坐标"""
            return self.coordinates.get(name, default)
        
        def has_coordinate(self, name):
            """检查是否存在指定名称的坐标"""
            return name in self.coordinates
        
        def get_all_coordinates(self):
            """获取所有坐标"""
            return self.coordinates.copy()
        
        def add_coordinate(self, name, x, y):
            """添加新坐标"""
            self.coordinates[name] = [x, y]
            self._save_coordinates()
        
        def _save_coordinates(self):
            """保存坐标到文件"""
            try:
                with open(self.file_path, "w", encoding="utf-8") as f:
                    json.dump(self.coordinates, f, ensure_ascii=False, indent=2)
                return True
            except Exception:
                return False
    
    # 使用坐标管理类
    manager = CoordinateManager()
    
    if manager.get_all_coordinates():
        print("坐标管理类已成功加载坐标数据")
        
        # 示例：使用坐标执行操作
        print("\n模拟使用坐标管理类执行操作:")
        
        # 检查是否有登录相关的坐标
        if manager.has_coordinate("login_button"):
            login_pos = manager.get_coordinate("login_button")
            print(f"点击登录按钮: {login_pos}")
        else:
            print("未找到登录按钮坐标")
        
        # 可以添加更多操作...
    else:
        print("当前没有保存的坐标数据")
        print("您可以使用以下代码添加坐标:")
        print("  manager.add_coordinate('test_point', 100, 200)")

# 方法4: 模拟自动化操作
def simulate_automation():
    """模拟使用坐标进行自动化操作"""
    print("\n方法4: 模拟自动化操作")
    
    # 这里只是示例，实际使用时需要安装pyautogui
    try:
        # 尝试导入pyautogui，实际使用时取消注释
        # import pyautogui
        
        print("注意: 以下是使用pyautogui进行自动化的示例代码")
        print("要运行实际的自动化操作，请取消注释相应的代码")
        print()
        
        print("# 自动化操作示例代码:")
        print("# import pyautogui")
        print("# pyautogui.PAUSE = 1  # 每个操作后暂停1秒")
        print()
        print("# 从坐标工具复制的坐标")
        print("# button1 = (100, 200)")
        print("# button2 = (300, 200)")
        print()
        print("# 执行自动化操作")
        print("# pyautogui.moveTo(button1)")
        print("# pyautogui.click()")
        print("# time.sleep(1)")
        print("# pyautogui.moveTo(button2)")
        print("# pyautogui.click()")
        
    except ImportError:
        print("提示: 要运行实际的自动化操作，需要安装pyautogui库:")
        print("  pip install pyautogui")

# 方法5: 创建可配置的坐标系统
def use_configurable_coordinates():
    """使用可配置的坐标系统"""
    print("\n方法5: 使用可配置的坐标系统")
    
    class ConfigurableCoordinateSystem:
        def __init__(self, base_resolution=(1920, 1080)):
            self.base_resolution = base_resolution
            self.current_resolution = None
            self.coordinates = {}
            
        def set_current_resolution(self, width, height):
            """设置当前屏幕分辨率"""
            self.current_resolution = (width, height)
            
        def load_base_coordinates(self, coordinates_dict):
            """加载基准分辨率下的坐标"""
            self.coordinates = coordinates_dict.copy()
            
        def get_adjusted_coordinate(self, name):
            """获取根据当前分辨率调整后的坐标"""
            if not self.current_resolution or name not in self.coordinates:
                return None
            
            # 获取基准坐标
            base_x, base_y = self.coordinates[name]
            
            # 计算缩放比例
            scale_x = self.current_resolution[0] / self.base_resolution[0]
            scale_y = self.current_resolution[1] / self.base_resolution[1]
            
            # 调整坐标
            adjusted_x = int(base_x * scale_x)
            adjusted_y = int(base_y * scale_y)
            
            return (adjusted_x, adjusted_y)
    
    # 示例使用
    print("创建基于分辨率的可配置坐标系统")
    print("这对于不同分辨率的屏幕适配非常有用")
    
    # 加载坐标数据
    coords = load_coordinates_from_json()
    
    if coords:
        # 创建坐标系统
        coord_system = ConfigurableCoordinateSystem()
        coord_system.load_base_coordinates(coords)
        
        # 设置当前分辨率
        coord_system.set_current_resolution(1366, 768)  # 示例分辨率
        
        # 获取调整后的坐标
        first_coord_name = list(coords.keys())[0]
        adjusted_coord = coord_system.get_adjusted_coordinate(first_coord_name)
        
        if adjusted_coord:
            original_coord = coords[first_coord_name]
            print(f"坐标 '{first_coord_name}' 调整:")
            print(f"  原始坐标 ({original_coord[0]}, {original_coord[1]}) -> 调整后坐标 {adjusted_coord}")

# 主函数
def main():
    """主函数"""
    print("坐标工具使用示例\n")
    
    # 展示不同的使用方法
    use_hardcoded_coordinates()
    load_coordinates_from_json()
    use_coordinate_manager()
    simulate_automation()
    use_configurable_coordinates()
    
    print("\n示例演示完成！")
    print("请根据您的实际需求选择适合的方法使用坐标数据。")

if __name__ == "__main__":
    main()