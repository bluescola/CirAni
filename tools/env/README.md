# CirAni 环境工具说明

本目录用于存放构建环境相关的工具。

## 目录结构

```
env/
├── scons/      # SCons 构建工具(可选,系统已有 scons)
├── kconfig/    # Kconfig 配置工具(如需要 menuconfig)
└── README.md   # 本文件
```

## 说明

与 D12x 的 `tools/env/` 不同,CirAni 是桌面应用,不需要打包完整的开发环境。

### 系统已有的工具

CirAni 依赖以下系统工具(需要预先安装):

```bash
# 编译工具
- gcc           # C 编译器
- g++           # C++ 编译器
- make          # Make 构建工具
- python3       # Python 3 解释器
- scons         # SCons 构建系统

# raylib 依赖库
- libgl1-mesa-dev   # OpenGL 开发库
- libx11-dev        # X11 窗口系统
- libpthread-stubs0-dev  # 线程库
```

### 安装方法 (Ubuntu/Debian)

```bash
# 基础编译工具
sudo apt install build-essential

# SCons
sudo apt install scons

# raylib 依赖
sudo apt install libgl1-mesa-dev libx11-dev

# Python 3 (通常已安装)
sudo apt install python3 python3-pip
```

### Kconfig 工具 (可选)

如果需要使用 `menuconfig` 进行图形化配置:

```bash
# 安装 kconfiglib
pip3 install kconfiglib

# 使用方法
cd /home/zane/project/raylib_pro/CirAni
menuconfig Kconfig
```

## 与 D12x 的区别

| 项目 | D12x | CirAni |
|------|------|--------|
| **环境打包** | ✅ 打包 Python 2.7 + SCons | ❌ 使用系统工具 |
| **目标平台** | 嵌入式(ARM) | 桌面(x86_64) |
| **工具链** | 打包交叉编译工具链 | 使用系统 GCC |
| **Kconfig** | 内置 | 需要单独安装 |

## 总结

CirAni 项目不需要像 D12x 一样打包完整的开发环境,只需确保系统安装了必要的编译工具即可。
