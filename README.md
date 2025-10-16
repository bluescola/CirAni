# CirAni - 电路科普动画项目

基于 raylib 的电路科普动画演示项目，使用 SCons 构建系统。

## 项目简介

这是一个用于学习 SCons 构建系统的示例项目，同时也是一个简单的电路动画演示程序。项目展示了：

- 如何使用 SCons 构建 C 语言项目
- 如何组织项目目录结构
- 如何使用 raylib 创建简单的动画效果

## 特性

- 完整的 SCons 构建配置（带详细注释）
- 源码和构建文件分离
- 快速构建脚本
- 简单的电路动画演示
- 增量编译支持

## 依赖

- GCC 编译器
- SCons 构建工具
- raylib 图形库

### 安装依赖（Ubuntu/Debian）

```bash
sudo apt-get update
sudo apt-get install build-essential scons
sudo apt-get install libraylib-dev
```

## 快速开始

### 1. 编译项目

```bash
# 方法一：使用 scons 直接编译
scons

# 方法二：使用快速构建脚本
./build.sh

# 方法三：使用 Python 辅助脚本
python3 tools/scripts/build.py
```

### 2. 运行程序

```bash
# 运行可执行文件
./bin/CirAni

# 或者编译并运行
./build.sh br
```

### 3. 清理构建文件

```bash
# 使用 scons 清理
scons -c

# 或使用快速脚本
./build.sh clean
```

## 项目结构

```
CirAni/
├── SConstruct              # SCons 主构建脚本
├── SConscript              # SCons 子构建脚本
├── build.sh                # Bash 快速构建脚本
├── README.md               # 项目说明
├── application/
│   └── src/
│       └── main.c          # 主程序源码
├── bin/                    # 可执行文件输出目录
├── build/                  # 构建临时文件目录
├── doc/
│   └── SCons学习指南.md   # SCons 学习文档
└── tools/
    └── scripts/
        └── build.py        # Python 构建辅助脚本
```

## 构建命令

### 基本命令

```bash
scons           # 编译项目
scons -c        # 清理构建文件
scons -j4       # 使用 4 个并行任务编译
scons -Q        # 安静模式
scons -h        # 查看帮助
```

### 使用构建脚本

```bash
./build.sh          # 编译
./build.sh clean    # 清理
./build.sh run      # 运行
./build.sh br       # 编译并运行
./build.sh help     # 帮助
```

## SCons 学习

本项目是学习 SCons 的绝佳起点：

1. **SConstruct 文件**：包含详细的中文注释，解释每个配置项
2. **SConscript 文件**：展示如何收集和编译源文件
3. **学习文档**：查看 `doc/SCons学习指南.md` 了解详细说明

### 核心概念

- **Environment（环境）**：包含编译器和编译选项的配置
- **variant_dir**：实现源码和构建文件分离
- **Import/Export**：在脚本之间传递变量
- **增量编译**：自动检测文件变化，只重新编译修改的文件

## 程序说明

运行程序后，你会看到一个简单的电路动画：

- 蓝色小球代表电子，沿着导线运动
- 左侧是电池符号（电源）
- 右侧是电阻符号
- 电子会沿着正弦轨迹运动，模拟电路中的电流

**操作**：
- 按 ESC 或关闭窗口退出

## 扩展建议

你可以基于这个项目进行以下扩展：

1. **添加更多电路元件**：如电容器、电感器等
2. **添加交互功能**：用鼠标控制电路参数
3. **多模块构建**：将不同功能分到不同的源文件
4. **添加构建配置**：如 Debug/Release 模式
5. **跨平台支持**：添加 Windows 和 macOS 的构建配置

## 常见问题

### 编译错误：找不到 raylib

确保已安装 raylib 开发库：
```bash
sudo apt-get install libraylib-dev
```

### 权限错误

给脚本添加执行权限：
```bash
chmod +x build.sh
```

### 修改头文件后没有重新编译

清理并重新构建：
```bash
scons -c && scons
```

## 参考资源

- [SCons 官方文档](https://scons.org/documentation.html)
- [raylib 官方网站](https://www.raylib.com/)
- [SCons 学习指南](doc/SCons学习指南.md)

## 许可证

本项目仅用于学习目的。

## 作者

创建于 2025 年，用于学习 SCons 构建系统。

---

**祝学习愉快！** 🚀
