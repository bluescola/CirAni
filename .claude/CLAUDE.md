# CirAni 项目上下文

## 项目概述

这是一个基于 raylib 的电路科普动画项目，同时也是学习 SCons 构建系统的实践项目。项目结构参考了匠芯创（Nuclei）的工程组织方式。

## 项目目标

1. **学习 SCons 构建系统**：通过实际项目掌握 SCons 的使用
2. **开发电路科普动画**：使用 raylib 创建直观的电路动画演示
3. **规范化工程结构**：采用专业的项目组织方式

## 技术栈

- **编程语言**: C
- **构建系统**: SCons
- **图形库**: raylib
- **开发环境**: Linux (WSL2)

## 项目结构

```
CirAni/
├── .claude/                # Claude Code 配置
│   └── CLAUDE.md          # 项目上下文（本文件）
├── .vscode/               # VS Code 配置
├── application/           # 应用代码
│   ├── demos/             # 示例程序
│   ├── src/               # 主程序源码
│   │   └── main.c         # 主程序入口
│   └── tutorials/         # 教程代码
├── build/                 # 构建临时文件（不提交）
├── doc/                   # 项目文档
│   ├── design/            # 设计文档
│   └── SCons学习指南.md
├── output/                # 配置输出目录（不提交）
│   ├── configs/           # 生成的配置文件
│   └── reports/           # 构建报告、日志等
├── packages/              # 外部依赖包
│   └── CirAni/            # 项目自定义包
├── patches/               # 补丁文件
│   └── raylib/            # raylib 补丁
├── target/                # 目标平台相关
│   ├── configs/           # 平台配置
│   ├── desktop_linux/     # Linux 平台
│   ├── desktop_macos/     # macOS 平台
│   └── desktop_windows/   # Windows 平台
├── tools/                 # 构建工具和脚本
│   ├── env/               # 环境配置
│   ├── raylib_tools/      # raylib 工具
│   ├── scripts/           # Python 脚本
│   │   └── build.py       # Python 构建辅助脚本
│   └── toolchain/         # 工具链
├── SConstruct             # SCons 主构建脚本
├── SConscript             # SCons 子构建脚本
├── build.sh               # Bash 快速构建脚本
├── .gitignore             # Git 忽略配置
├── Kconfig                # 配置系统（预留）
├── ReleaseNote.md         # 发布说明
└── README.md              # 项目说明
```

## 构建说明

### 快速构建命令

```bash
# 编译项目
scons                    # 标准方式
./build.sh               # 快速脚本
python3 tools/scripts/build.py  # Python 脚本

# 运行程序
./CirAni                 # 可执行文件输出在项目根目录
./build.sh br            # 编译并运行

# 清理
scons -c
./build.sh clean
```

### 构建系统特点

- **源码与构建分离**: 使用 `variant_dir` 保持源码目录整洁
- **增量编译**: 自动检测文件变化，只重新编译修改的文件
- **详细注释**: SConstruct 和 SConscript 包含详细中文注释
- **多种构建方式**: 支持 scons、bash、python 多种构建入口

## 当前实现功能

### 动画效果
- 蓝色小球代表电子，沿导线运动
- 左侧电池符号（电源）
- 右侧电阻符号
- 电子沿正弦轨迹运动，模拟电路中的电流

### 交互
- ESC 键或关闭窗口退出

## 开发规范

### 代码风格
- C 语言标准：C11
- 编译器：GCC
- 警告级别：-Wall（所有警告）

### 目录组织原则
1. **application/**: 应用层代码，包含 main 函数和业务逻辑
2. **packages/**: 第三方库和依赖包
3. **tools/**: 构建工具、脚本、辅助程序
4. **target/**: 目标平台相关的配置和代码
5. **doc/**: 文档和学习资料
6. **output/**: 配置输出和构建报告（自动生成的文件）

### Git 管理
- 不提交 `build/` 和 `output/` 目录
- 不提交 `.sconsign.dblite` 缓存文件
- 不提交编译产物(可执行文件在项目根目录)

## 扩展方向

### 短期目标
- [ ] 添加更多电路元件（电容、电感等）
- [ ] 实现电路参数调节功能
- [ ] 添加用户交互（鼠标控制）
- [ ] 完善动画效果和视觉呈现

### 长期规划
- [ ] 多模块化代码结构（将功能拆分到多个源文件）
- [ ] 添加 Debug/Release 构建配置
- [ ] 跨平台支持（Windows、macOS）
- [ ] 配置系统集成（使用 Kconfig）
- [ ] 单元测试框架

## 学习资源

- **SCons 官方文档**: https://scons.org/documentation.html
- **raylib 官方网站**: https://www.raylib.com/
- **项目内文档**: `doc/SCons学习指南.md`

## 注意事项

1. **依赖安装**: 确保系统已安装 gcc、scons 和 libraylib-dev
2. **脚本权限**: 首次使用需要给 build.sh 添加执行权限
3. **头文件变化**: 修改头文件后建议清理重建（`scons -c && scons`）
4. **路径问题**: 所有构建命令应在项目根目录（CirAni/）执行

## 项目历史

- **创建时间**: 2025-10
- **创建方式**: 通过 Claude Code 协助构建
- **参考项目**: 匠芯创（Nuclei）工程结构
- **设计理念**: 学习与实践相结合，规范化工程组织

---

**使用建议**:
- 修改代码时，参考 SConstruct 中的注释理解构建流程
- 添加新功能前，先阅读相关文档
- 保持代码简洁清晰，添加必要的注释
- 每次重要更新后更新 ReleaseNote.md
