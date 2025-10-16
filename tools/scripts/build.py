#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
构建辅助脚本
提供一些常用的构建功能
"""

import os
import sys
import subprocess
import shutil

# 项目根目录
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def run_command(cmd, cwd=None):
    """运行命令并显示输出"""
    print(f"执行: {cmd}")
    if cwd is None:
        cwd = PROJECT_ROOT
    result = subprocess.run(cmd, shell=True, cwd=cwd)
    return result.returncode

def build():
    """编译项目"""
    print("=" * 50)
    print("开始编译项目...")
    print("=" * 50)
    return run_command("scons")

def build_parallel(jobs=4):
    """并行编译项目"""
    print("=" * 50)
    print(f"使用 {jobs} 个并行任务编译项目...")
    print("=" * 50)
    return run_command(f"scons -j{jobs}")

def clean():
    """清理构建文件"""
    print("=" * 50)
    print("清理构建文件...")
    print("=" * 50)
    return run_command("scons -c")

def rebuild():
    """重新编译"""
    print("=" * 50)
    print("重新编译项目...")
    print("=" * 50)
    clean()
    return build()

def run_program():
    """运行程序"""
    print("=" * 50)
    print("运行程序...")
    print("=" * 50)
    bin_path = os.path.join(PROJECT_ROOT, "bin", "CirAni")
    if not os.path.exists(bin_path):
        print(f"错误: 可执行文件不存在: {bin_path}")
        print("请先编译项目")
        return 1
    return run_command(bin_path)

def build_and_run():
    """编译并运行"""
    ret = build()
    if ret == 0:
        return run_program()
    return ret

def show_help():
    """显示帮助信息"""
    print("""
========================================
CirAni 构建辅助脚本
========================================

使用方法：
  python3 build.py [命令]

可用命令：
  build        - 编译项目 (默认)
  parallel     - 并行编译（4线程）
  clean        - 清理构建文件
  rebuild      - 重新编译（清理后编译）
  run          - 运行程序
  br           - 编译并运行
  help         - 显示此帮助信息

示例：
  python3 build.py             # 编译项目
  python3 build.py parallel    # 并行编译
  python3 build.py clean       # 清理
  python3 build.py br          # 编译并运行

========================================
""")

def main():
    """主函数"""
    # 切换到项目根目录
    os.chdir(PROJECT_ROOT)

    # 获取命令
    command = sys.argv[1] if len(sys.argv) > 1 else "build"

    # 执行命令
    commands = {
        "build": build,
        "parallel": build_parallel,
        "clean": clean,
        "rebuild": rebuild,
        "run": run_program,
        "br": build_and_run,
        "help": show_help,
    }

    if command in commands:
        return commands[command]()
    else:
        print(f"未知命令: {command}")
        show_help()
        return 1

if __name__ == "__main__":
    sys.exit(main())
