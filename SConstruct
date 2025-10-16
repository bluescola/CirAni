import os
import sys

# 获取项目根目录
CIRANI_ROOT = os.path.normpath(os.getcwd())
print("SConstruct path:", CIRANI_ROOT)

# 导入辅助函数
cirani_script_path = os.path.join(CIRANI_ROOT, 'tools/scripts') #添加路径
print("辅助脚本路径：",cirani_script_path)

if os.path.exists(cirani_script_path):
        sys.path.append(cirani_script_path)     #脚本目录添加到Python搜索路径
else:
        print(f"辅助脚本路径错误：{cirani_script_path}") #f {}语法更适合多变量的格式化
        Exit(1) # scons退出，小写是python的，大写更规范

from cirani_build import *      #导入cirani_build.py所有函数

# 读取项目配置
PRJ_TARGET = os.path.join(CIRANI_ROOT,"target/configs")
append_path_if_exists(PRJ_TARGET,"项目配置路径")


