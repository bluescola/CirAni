# raylib 集成到 CirAni 项目指南

## 文档说明

本文档详细说明如何将 `/home/zane/src/raylib` 中的各个组件正确集成到 CirAni 项目中。

**raylib 源码位置**: `/home/zane/src/raylib`

---

## 一、raylib 目录结构分析

### raylib 完整结构
```
/home/zane/src/raylib/
├── src/                      # raylib 核心源码
│   ├── raylib.h             # ★ 主头文件
│   ├── raymath.h            # 数学库
│   ├── rcamera.h            # 相机
│   ├── rlgl.h               # OpenGL抽象层
│   ├── rcore.c              # 核心功能
│   ├── raudio.c             # 音频
│   ├── rtext.c              # 文字渲染
│   ├── rtextures.c          # 纹理
│   ├── rshapes.c            # 2D图形
│   ├── rmodels.c            # 3D模型
│   ├── utils.c/h            # 工具函数
│   ├── libraylib.a          # 已编译的静态库
│   ├── external/            # 外部依赖(glfw, stb等)
│   └── platforms/           # 平台相关代码
│
├── examples/                 # 示例代码(160+个)
│   ├── core/
│   ├── shapes/
│   ├── textures/
│   ├── text/
│   ├── models/
│   ├── audio/
│   └── ...
│
├── tools/                    # raylib 开发工具
│   ├── rexm/                # raylib examples manager(示例管理工具)
│   └── rlparser/            # raylib parser(API解析工具)
│
├── projects/                 # 各种IDE项目文件
│   ├── VS2022/
│   ├── CMake/
│   └── ...
│
├── CMakeLists.txt           # CMake 构建配置
├── Makefile                 # Makefile 构建
└── README.md
```

---

## 二、raylib 各组件在 CirAni 中的位置

### 2.1 核心库文件 → `packages/CirAni/raylib/`

**原路径**: `/home/zane/src/raylib/src/`
**目标位置**: `packages/CirAni/raylib/`

**集成方式**: 软链接(推荐)

```bash
cd /home/zane/project/raylib_pro/CirAni/packages/CirAni/raylib/

# 方案1: 链接整个src目录
ln -s /home/zane/src/raylib/src src

# 方案2: 链接关键文件
ln -s /home/zane/src/raylib/src/raylib.h raylib.h
ln -s /home/zane/src/raylib/src/raymath.h raymath.h
ln -s /home/zane/src/raylib/src/rcamera.h rcamera.h
ln -s /home/zane/src/raylib/src/rlgl.h rlgl.h
ln -s /home/zane/src/raylib/src/libraylib.a libraylib.a

# 方案3: 使用系统安装的 raylib
# 在 SConscript 中: env.Append(LIBS=['raylib'])
```

**结果目录结构**:
```
packages/CirAni/raylib/
├── src -> /home/zane/src/raylib/src  (软链接)
├── SConscript                         (您编写)
└── README.md                          (说明文件)
```

---

### 2.2 raylib 工具 → `tools/raylib_tools/`

**原路径**: `/home/zane/src/raylib/tools/`
**目标位置**: `tools/raylib_tools/` (专门放置 raylib 相关工具)

**为什么不放在 `packages/CirAni/raylib/tools/`?**
- 因为这些工具是**开发工具**,不是运行时库
- 参考 D12x 的 `tools/` 目录,专门放置开发工具

**集成方式**: 软链接

```bash
cd /home/zane/project/raylib_pro/CirAni/tools/

# 链接 raylib 工具目录
ln -s /home/zane/src/raylib/tools raylib_tools
```

**raylib 工具说明**:

#### 1. **rexm** - raylib examples manager
**功能**: 管理 raylib 示例集合
- 添加、重命名、删除示例
- 验证示例完整性
- 构建示例(桌面和Web)

**对 CirAni 的用途**:
- 您可以参考学习如何管理演示案例
- 可能用于管理 `application/demos/` 和 `application/tutorials/`

**使用**:
```bash
cd tools/raylib_tools/rexm
make  # 编译 rexm
./rexm --help
```

#### 2. **rlparser** - raylib API 解析器
**功能**: 解析 `raylib.h` 生成 API 文档
- 提取函数、结构体、枚举定义
- 导出为 JSON、XML、Lua 等格式

**对 CirAni 的用途**:
- 您可能用于生成 CirAni API 文档
- 解析 `packages/CirAni/include/` 中的头文件

**使用**:
```bash
cd tools/raylib_tools/rlparser
make  # 编译 rlparser
./rlparser --input raylib.h --output api.json
```

---

### 2.3 raylib 示例 → 参考学习,不集成

**原路径**: `/home/zane/src/raylib/examples/`
**处理方式**: 不复制到 CirAni,仅作为学习参考

**为什么不集成?**
- raylib 有 160+ 个示例,太多了
- CirAni 的 `application/demos/` 是您自己的演示,功能不同

**学习方式**:
```bash
# 查看 raylib 示例
cd /home/zane/src/raylib/examples/

# 编译运行示例
cd core
make core_basic_window
./core_basic_window
```

---

### 2.4 raylib 构建配置 → 不集成

**原路径**:
- `/home/zane/src/raylib/CMakeLists.txt`
- `/home/zane/src/raylib/Makefile`

**处理方式**: CirAni 使用 SCons,不使用 raylib 的构建系统

**但可以参考**:
- 查看编译选项
- 查看链接库列表

---

## 三、CirAni 目录结构(更新后)

```
CirAni/
├── packages/
│   └── CirAni/
│       ├── raylib/                    # raylib 库
│       │   ├── src -> /home/zane/src/raylib/src  (软链接)
│       │   ├── SConscript             (编译配置)
│       │   └── README.md
│       ├── components/                # 您的元件库
│       ├── animation/                 # 您的动画引擎
│       ├── circuit/                   # 您的电路仿真
│       ├── graphics/                  # 您的渲染封装(基于raylib)
│       └── common/                    # 您的通用工具
│
├── tools/
│   ├── scripts/                       # 您的构建脚本
│   │   ├── cirani_build.py
│   │   └── ...
│   ├── env/                           # 环境工具
│   │   ├── scons/
│   │   └── kconfig/
│   ├── raylib_tools -> /home/zane/src/raylib/tools  (软链接)
│   │   ├── rexm/                      # raylib 示例管理器
│   │   └── rlparser/                  # raylib API 解析器
│   ├── onestep.sh
│   └── build.sh
│
└── (其他目录...)
```

---

## 四、packages/CirAni/raylib/SConscript 实现

### 方案1: 链接已编译的 libraylib.a (最简单)

```python
Import('CIRANI_ROOT')
import os

# raylib 目录
raylib_dir = os.path.join(CIRANI_ROOT, 'packages/CirAni/raylib')

# 添加头文件路径
env.Append(CPPPATH=[
    os.path.join(raylib_dir, 'src'),
])

# 链接静态库
env.Append(LIBS=[
    File(os.path.join(raylib_dir, 'src/libraylib.a'))
])

# 添加 raylib 依赖的系统库
env.Append(LIBS=['GL', 'm', 'pthread', 'dl', 'rt', 'X11'])

# 不编译,只返回空列表
objs = []
Return('objs')
```

### 方案2: 使用系统安装的 raylib (适合发布)

```python
Import('CIRANI_ROOT')
import os

# 使用系统 raylib
env.Append(LIBS=['raylib'])

# 系统头文件路径(如果需要)
env.Append(CPPPATH=['/usr/include'])

# raylib 依赖
env.Append(LIBS=['GL', 'm', 'pthread', 'dl', 'rt', 'X11'])

objs = []
Return('objs')
```

### 方案3: 从源码编译 raylib (最完整,但复杂)

```python
Import('CIRANI_ROOT')
import os

raylib_src_dir = os.path.join(CIRANI_ROOT, 'packages/CirAni/raylib/src')

# raylib 源文件
raylib_sources = [
    'rcore.c',
    'rshapes.c',
    'rtextures.c',
    'rtext.c',
    'rmodels.c',
    'raudio.c',
    'rglfw.c',
    'utils.c',
]

# 添加头文件路径
env.Append(CPPPATH=[
    raylib_src_dir,
    os.path.join(raylib_src_dir, 'external'),
    os.path.join(raylib_src_dir, 'external/glfw/include'),
])

# 编译选项
env.Append(CFLAGS=[
    '-DPLATFORM_DESKTOP',
    '-DGRAPHICS_API_OPENGL_33',
])

# 编译 raylib 源文件
objs = []
for src in raylib_sources:
    src_path = os.path.join(raylib_src_dir, src)
    objs += env.Object(src_path)

# 链接依赖库
env.Append(LIBS=['GL', 'm', 'pthread', 'dl', 'rt', 'X11'])

Return('objs')
```

---

## 五、实施步骤

### 步骤1: 创建软链接

```bash
cd /home/zane/project/raylib_pro/CirAni

# 1. 链接 raylib 源码
cd packages/CirAni/raylib/
ln -s /home/zane/src/raylib/src src
cd ../../..

# 2. 链接 raylib 工具
cd tools/
ln -s /home/zane/src/raylib/tools raylib_tools
cd ..
```

### 步骤2: 创建 README.md 说明文件

**位置**: `packages/CirAni/raylib/README.md`

```markdown
# raylib 集成说明

本目录包含 raylib 图形库的集成。

## raylib 简介

raylib 是一个简单易用的游戏开发库,用于2D/3D图形、音频、输入等。

官网: https://www.raylib.com/
源码: https://github.com/raysan5/raylib

## 当前集成方式

- **方式**: 软链接到本地 raylib 源码
- **源码位置**: `/home/zane/src/raylib`
- **链接位置**: `src -> /home/zane/src/raylib/src`

## 编译方式

参见 `SConscript` 文件。

## 依赖库

raylib 需要以下系统库:
- OpenGL (libGL)
- 数学库 (libm)
- 线程库 (pthread)
- 动态链接库 (dl)
- 实时扩展 (rt)
- X11 窗口系统 (libX11)

## 安装依赖 (Ubuntu/Debian)

```bash
sudo apt install libgl1-mesa-dev libx11-dev
```
```

### 步骤3: 编写 packages/CirAni/raylib/SConscript

参考上面的三个方案,选择一个实现。**推荐方案1**(最简单)。

### 步骤4: 测试编译

```bash
# 测试链接是否正常
ls -la packages/CirAni/raylib/src/raylib.h
ls -la tools/raylib_tools/rexm/

# 尝试编译(需要先完成 SConstruct 和其他文件)
scons
```

---

## 六、raylib 工具的使用

### 6.1 编译 raylib 工具

```bash
# 编译 rexm
cd tools/raylib_tools/rexm
make
./rexm --help

# 编译 rlparser
cd ../rlparser
make
./rlparser --help
```

### 6.2 可能的使用场景

#### 场景1: 生成 CirAni API 文档

```bash
cd tools/raylib_tools/rlparser

# 解析您的 CirAni 头文件
./rlparser --input ../../../packages/CirAni/include/cirani.h \
           --output ../../../doc/api/cirani_api.json \
           --format JSON \
           --define CIRANI_API
```

#### 场景2: 管理演示案例

参考 rexm 的实现,为 CirAni 创建类似的工具管理 `application/demos/`。

---

## 七、常见问题

### Q1: 软链接在 Git 中会被提交吗?
A: 会!但只是链接本身(几个字节),不是目标文件。
   - 其他人克隆后,需要调整链接指向自己的 raylib 路径
   - 或者在文档中说明如何安装 raylib

### Q2: 为什么不直接复制 raylib 源码?
A:
   - raylib 经常更新,复制不便于同步
   - 软链接可以随时更新到最新版本
   - 节省空间

### Q3: 发布时怎么办?
A: 三种方案:
   1. 要求用户安装 raylib (推荐)
   2. 静态链接 raylib
   3. 提供预编译的二进制文件

### Q4: raylib 工具必须集成吗?
A: 不是必须的。
   - `rexm` 主要用于管理 raylib 自己的示例
   - `rlparser` 可以用于生成文档,但不是必需的
   - 您可以先不集成,需要时再添加

---

## 八、总结

### raylib 在 CirAni 中的位置

| raylib 组件 | 原路径 | CirAni 中的位置 | 集成方式 |
|------------|--------|----------------|---------|
| 核心源码 | `/home/zane/src/raylib/src/` | `packages/CirAni/raylib/src/` | 软链接 |
| 开发工具 | `/home/zane/src/raylib/tools/` | `tools/raylib_tools/` | 软链接 |
| 示例代码 | `/home/zane/src/raylib/examples/` | 不集成 | 仅供参考 |
| 构建配置 | `/home/zane/src/raylib/CMakeLists.txt` | 不集成 | 仅供参考 |

### 下一步

1. ✅ 创建软链接
2. ✅ 编写 `packages/CirAni/raylib/SConscript`
3. ✅ 测试编译链接
4. ⬜ (可选) 编译 raylib 工具

---

**文档版本**: v1.0
**创建日期**: 2025-10-16
**维护者**: CirAni Team
