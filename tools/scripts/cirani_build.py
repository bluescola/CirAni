#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# CirAni 构建辅助工具
# 参考 D12x 的 aic_build.py

import os
import sys

# ANSI 颜色代码 (前景色 - 字体颜色)
COLOR_BEGIN = "\033["
COLOR_RED = COLOR_BEGIN + "31m"      # 红色字
COLOR_YELLOW = COLOR_BEGIN + "33m"   # 黄色字
COLOR_WHITE = COLOR_BEGIN + "37m"    # 白色字
COLOR_GREEN = COLOR_BEGIN + "32m"    # 绿色字
COLOR_END = "\033[0m"


def pr_err(string):
    """打印错误信息(红色字体)"""
    print(COLOR_RED + '*** ' + string + COLOR_END)


def pr_info(string):
    """打印信息(绿色字体)"""
    print(COLOR_GREEN + '>>> ' + string + COLOR_END)


def pr_warn(string):
    """打印警告(黄色字体)"""
    print(COLOR_YELLOW + '!!! ' + string + COLOR_END)


def pr_raw(string):
    """打印原始信息(白色字体)"""
    print(COLOR_WHITE + '--- ' + string + COLOR_END)


def chk_prj_config(root):
    """
    检查项目配置是否存在

    Args:
        root: 项目根目录
    """
    config_file = os.path.join(root, '.config')
    if not os.path.exists(config_file):
        pr_warn(f"配置文件 {config_file} 不存在")
        pr_info("使用默认配置")
        return False
    return True


def get_prj_config(root):
    """
    读取项目配置

    Args:
        root: 项目根目录

    Returns:
        tuple: (PRJ_TARGET, PRJ_APP)

    示例:
        PRJ_TARGET = 'desktop_linux'
        PRJ_APP = 'basic_circuit'
    """
    config_file = os.path.join(root, '.config')

    # 默认配置
    prj_target = 'desktop_linux'
    prj_app = 'basic_circuit'

    if not os.path.exists(config_file):
        pr_warn("未找到 .config 文件,使用默认配置")
        return prj_target, prj_app

    # 读取配置文件
    try:
        with open(config_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith('CONFIG_PRJ_TARGET='):
                    prj_target = line.split('=')[1].strip('"')
                elif line.startswith('CONFIG_PRJ_APP='):
                    prj_app = line.split('=')[1].strip('"')
    except Exception as e:
        pr_err(f"读取配置文件失败: {e}")
        return prj_target, prj_app

    pr_info(f"项目配置: TARGET={prj_target}, APP={prj_app}")
    return prj_target, prj_app


def get_config_value(config_file, key):
    """
    从配置文件中获取指定键的值

    Args:
        config_file: 配置文件路径
        key: 配置键名

    Returns:
        str: 配置值,未找到返回 None
    """
    if not os.path.exists(config_file):
        return None

    try:
        with open(config_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith(key + '='):
                    value = line.split('=', 1)[1].strip('"')
                    return value
    except Exception as e:
        pr_err(f"读取配置失败: {e}")

    return None

def append_path_if_exists(path_or_file,path_info):
    '''
    文件直接添加父目录到sys.path
    路径添加到sys.path
    '''
    if not os.path.exists(path_or_file):
        pr_warn(f"{path_or_file}不存在")
        return False

    if os.path.isfile(path_or_file):
        target_path = os.path.dirname(path_or_file)
        if not target_path:  # 防止空路径
                pr_err(f"{path_info}无法获取父目录: {path_or_file}")
                return False
        pr_raw(f"{path_info}(文件->父目录):{target_path}已添加到sys.path")
    else:
        target_path = path_or_file
        pr_raw(f"{path_info}(目录),{path_or_file}已添加到sys.path")
    sys.path.append(target_path)
    return True


# 函数别名(简写)
pe = pr_err   # error
pw = pr_warn  # warning
pi = pr_info  # info
pr = pr_raw   # raw


if __name__ == '__main__':
    # 测试代码
    print("CirAni Build Utility")
    print("=" * 50)

    # 假设在项目根目录运行
    root = os.getcwd()

    pr_info("检查项目配置...")
    chk_prj_config(root)

    pr_info("读取项目配置...")
    target, app = get_prj_config(root)

    print("=" * 50)
    print(f"目标平台: {target}")
    print(f"应用程序: {app}")
