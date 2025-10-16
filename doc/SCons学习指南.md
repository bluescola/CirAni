# SCons 构建系统学习指南

## 项目介绍

CirAni 是一个基于 raylib 的电路科普动画项目，使用 SCons 作为构建系统。本文档将帮助你理解 SCons 的核心概念和使用方法。

## 目录结构

```
CirAni/
├── SConstruct              # 主构建脚本（核心配置）
├── SConscript              # 子构建脚本（源文件管理）
├── build.sh                # 快速构建脚本
├── application/
│   └── src/
│       └── main.c          # 应用程序源代码
├── bin/                    # 可执行文件输出目录
│   └── CirAni              # 最终可执行文件
├── build/                  # 构建临时文件（.o文件等）
└── tools/
    └── scripts/
        └── build.py        # Python 构建辅助脚本
```

## SCons 核心概念

### 1. SConstruct vs SConscript

- **SConstruct**: 主构建脚本，位于项目根目录
  - 配置编译器和编译选项
  - 设置头文件路径和库
  - 定义构建目标
  - 调用子构建脚本

- **SConscript**: 子构建脚本，可以有多个
  - 收集源文件
  - 编译源文件为目标文件
  - 返回目标文件列表给主脚本

### 2. Environment（环境）

Environment 是 SCons 的核心概念，包含所有编译工具和配置：

```python
# 创建默认环境
env = DefaultEnvironment()

# 设置编译器
env['CC'] = 'gcc'
env['CXX'] = 'g++'

# 添加编译选项
env.Append(CFLAGS=['-Wall', '-O2'])
env.Append(CPPPATH=['include'])  # 头文件路径
env.Append(LIBS=['raylib'])       # 链接库
```

### 3. variant_dir（变体目录）

这是 SCons 的重要特性，用于实现源码和构建文件的分离：

```python
objs = SConscript('SConscript',
                  variant_dir='build',  # 构建文件输出到 build 目录
                  duplicate=0)          # 不复制源文件，节省空间
```

**优点**：
- 保持源码目录整洁
- 可以同时构建多个配置（Debug、Release）
- 便于清理构建文件

### 4. Import/Export（导入/导出）

用于在 SConstruct 和 SConscript 之间传递变量：

```python
# 在 SConstruct 中导出
Export('env', 'ROOT_DIR', 'SRC_DIR')

# 在 SConscript 中导入
Import('env', 'ROOT_DIR', 'SRC_DIR')
```

### 5. 编译流程

```
SConstruct (配置环境)
    ↓
SConscript (收集源文件)
    ↓
编译源文件 → 目标文件 (.o)
    ↓
链接 → 可执行文件
```

## 使用方法

### 基本命令

```bash
# 编译项目
scons

# 清理构建文件
scons -c

# 并行编译（4个任务）
scons -j4

# 安静模式（减少输出）
scons -Q

# 查看帮助
scons -h
```

### 使用快速构建脚本

```bash
# 编译项目
./build.sh

# 清理
./build.sh clean

# 编译并运行
./build.sh br

# 查看帮助
./build.sh help
```

### 使用 Python 辅助脚本

```bash
cd tools/scripts

# 编译
python3 build.py build

# 并行编译
python3 build.py parallel

# 编译并运行
python3 build.py br

# 清理
python3 build.py clean
```

## SCons 常用方法

### 编译相关

```python
# 编译源文件为目标文件
obj = env.Object('main.c')

# 编译多个源文件
objs = env.Object(['file1.c', 'file2.c'])

# 链接生成可执行文件
program = env.Program('myapp', objs)

# 创建静态库
lib = env.Library('mylib', ['lib1.c', 'lib2.c'])

# 创建动态库
shlib = env.SharedLibrary('mylib', ['lib1.c', 'lib2.c'])
```

### 文件搜索

```python
# 使用 Glob 搜索文件
sources = Glob('src/*.c')

# 递归搜索
sources = Glob('src/**/*.c', recursive=True)
```

### 路径操作

```python
# 获取当前脚本所在目录
ROOT_DIR = Dir('#').abspath  # '#' 表示 SConstruct 所在目录

# 拼接路径
src_path = os.path.join(ROOT_DIR, 'src')
```

## 增量编译

SCons 的一大优势是自动增量编译：

1. **依赖追踪**：自动检测文件变化和依赖关系
2. **智能重编译**：只重新编译修改过的文件
3. **签名机制**：使用 MD5 签名检测文件内容变化

**示例**：
```bash
# 第一次编译（完整编译）
$ scons
gcc -o main.o -c main.c
gcc -o app main.o -lraylib

# 修改 main.c 后再次编译（只重编译 main.c）
$ scons
gcc -o main.o -c main.c
gcc -o app main.o -lraylib

# 如果没有修改任何文件
$ scons
scons: `.' is up to date.
```

## 实用技巧

### 1. 添加调试/发布模式

可以在 SConstruct 中添加构建模式支持：

```python
# 获取构建模式
build_mode = ARGUMENTS.get('mode', 'release')

if build_mode == 'debug':
    env.Append(CFLAGS=['-g', '-O0'])
    env.Append(CPPDEFINES=['DEBUG'])
else:
    env.Append(CFLAGS=['-O2'])
    env.Append(CPPDEFINES=['NDEBUG'])
```

使用：
```bash
scons mode=debug    # 调试模式
scons mode=release  # 发布模式
```

### 2. 自动依赖扫描

SCons 自动扫描头文件依赖：

```python
# SCons 会自动处理 #include 依赖
# 如果头文件修改，相关源文件会自动重新编译
```

### 3. 自定义清理

```python
# 添加额外的清理目标
Clean(program, ['build', 'bin', 'logs'])
```

### 4. 多模块项目

对于大型项目，可以在不同目录使用多个 SConscript：

```python
# 在 SConstruct 中
lib_objs = SConscript('lib/SConscript', variant_dir='build/lib')
app_objs = SConscript('app/SConscript', variant_dir='build/app')

# 合并目标文件
all_objs = lib_objs + app_objs
program = env.Program('myapp', all_objs)
```

## 常见问题

### Q: 为什么修改头文件后相关文件没有重新编译？

A: SCons 默认会扫描头文件依赖。如果没有自动重新编译，可能是缓存问题，尝试：
```bash
scons -c  # 清理
scons     # 重新构建
```

### Q: 如何加快编译速度？

A: 使用并行编译：
```bash
scons -j4  # 使用4个并行任务
scons -j$(nproc)  # 使用所有CPU核心
```

### Q: 如何查看详细的编译命令？

A: 默认 SCons 会显示编译命令。如果输出被精简，可以：
```bash
scons --verbose
```

## 学习资源

- SCons 官方文档: https://scons.org/documentation.html
- SCons 用户手册: https://scons.org/doc/production/HTML/scons-user.html
- 本项目源码: 查看 `SConstruct` 和 `SConscript` 文件中的详细注释

## 练习建议

1. **修改编译选项**：尝试在 `SConstruct` 中添加不同的编译标志
2. **添加新源文件**：创建新的 `.c` 文件并添加到 `SConscript`
3. **多模块构建**：尝试创建多个子目录，每个都有自己的 `SConscript`
4. **自定义目标**：学习创建自定义的构建目标（如文档生成）

## 总结

SCons 的主要优势：

1. **Python 语法**：易于学习和扩展
2. **自动依赖追踪**：智能增量编译
3. **跨平台**：在 Linux、Windows、macOS 上都能使用
4. **灵活配置**：可以轻松配置复杂的构建流程

通过这个项目，你已经掌握了 SCons 的核心概念。继续探索和实践，你会发现 SCons 是一个强大而灵活的构建工具！
