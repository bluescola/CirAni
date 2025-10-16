# SCons 内置函数参考

## 为什么 IDE 无法跳转到 SCons 函数源码？

SCons 的构建脚本（SConstruct/SConscript）看起来像普通的 Python 脚本，但实际上它们是在 SCons 的特殊执行环境中运行的。

**关键点**：
1. 这些函数不是通过 `import` 导入的
2. SCons 在执行构建脚本时，会将这些函数**注入到全局命名空间**
3. 这就是为什么你可以直接使用 `DefaultEnvironment()`、`Dir()` 等函数，而不需要导入
4. 这也是为什么 IDE 无法识别和跳转到这些函数的定义

## SCons 源码位置

### 系统安装位置
```
/usr/lib/python3/dist-packages/SCons/
```

### 核心模块
- **SCons/Script/__init__.py** - 主脚本模块，定义全局函数
- **SCons/Script/SConscript.py** - SConscript 相关函数
- **SCons/Environment.py** - 环境对象实现
- **SCons/Defaults.py** - 默认配置和环境
- **SCons/Node/FS.py** - 文件系统节点（Dir、File 等）

## 常用函数源码位置

### 1. DefaultEnvironment()
- **定义位置**: `/usr/lib/python3/dist-packages/SCons/Defaults.py`
- **导出位置**: `/usr/lib/python3/dist-packages/SCons/Script/__init__.py:174`
- **说明**: 创建或返回默认构建环境

```python
# 在 SCons/Script/__init__.py 中
DefaultEnvironment = SCons.Defaults.DefaultEnvironment
```

### 2. Dir() / File()
- **定义位置**: `/usr/lib/python3/dist-packages/SCons/Node/FS.py`
- **说明**: 创建目录节点或文件节点对象
- **用法**:
  - `Dir('path')` - 返回目录节点
  - `File('path')` - 返回文件节点

### 3. Export() / Import()
- **定义位置**: `/usr/lib/python3/dist-packages/SCons/Script/SConscript.py`
- **说明**: 在构建脚本之间传递变量
- **工作原理**: SCons 维护一个全局的导出字典

```python
# Export 的使用
Export('env', 'debug_mode')  # 导出变量供其他脚本使用

# Import 的使用
Import('env')  # 从父脚本导入变量
```

### 4. SConscript()
- **定义位置**: `/usr/lib/python3/dist-packages/SCons/Script/SConscript.py`
- **导出位置**: `/usr/lib/python3/dist-packages/SCons/Script/__init__.py:396`
- **说明**: 执行子构建脚本

```python
# 在 SCons/Script/__init__.py 中
SConscript = _SConscript.DefaultEnvironmentCall('SConscript')
```

### 5. Default()
- **说明**: 设置默认构建目标
- **用法**: `Default(target)` - 当不指定目标时构建此目标

### 6. Clean()
- **说明**: 注册清理操作
- **用法**: `Clean(target, files)` - 清理 target 时删除 files

### 7. Help()
- **说明**: 添加帮助信息
- **用法**: `Help(text)` - 添加到 `scons -h` 的输出

## 如何查看 SCons 函数源码

### 方法 1: 使用命令行查看
```bash
# 查找函数定义
grep -r "def DefaultEnvironment" /usr/lib/python3/dist-packages/SCons/

# 查找函数导出
grep -n "DefaultEnvironment" /usr/lib/python3/dist-packages/SCons/Script/__init__.py
```

### 方法 2: 在 Python 中查看
```bash
python3 -c "
import SCons.Defaults
import inspect
print(inspect.getsourcefile(SCons.Defaults.DefaultEnvironment))
"
```

### 方法 3: 直接打开源码文件
```bash
# 使用你喜欢的编辑器
code /usr/lib/python3/dist-packages/SCons/Script/__init__.py
code /usr/lib/python3/dist-packages/SCons/Defaults.py
```

## SCons 函数注入机制

SCons 通过以下步骤让这些函数可用：

1. **SCons 启动** - 执行 `scons` 命令时，运行 `SCons.Script.Main.main()`
2. **导入核心模块** - 加载 `SCons.Script.__init__.py`
3. **创建执行环境** - 创建一个特殊的全局命名空间
4. **注入函数** - 将内置函数添加到全局命名空间
5. **执行构建脚本** - 在这个特殊环境中执行 SConstruct

```python
# SCons 内部大致流程（简化版）
global_dict = {
    'DefaultEnvironment': SCons.Defaults.DefaultEnvironment,
    'Dir': some_dir_function,
    'Export': some_export_function,
    'Import': some_import_function,
    'SConscript': some_sconscript_function,
    'Default': some_default_function,
    'Clean': some_clean_function,
    'Help': some_help_function,
    # ... 更多函数
}

# 在这个环境中执行 SConstruct
exec(open('SConstruct').read(), global_dict)
```

## 为 IDE 添加代码提示

虽然 IDE 无法跳转到源码，但可以添加类型提示：

### 方法 1: 创建 stub 文件
创建 `scons_stubs.py` 文件（仅用于 IDE 提示，不实际导入）：

```python
# scons_stubs.py - SCons 函数类型提示
from typing import Any, List, Dict

def DefaultEnvironment(**kwargs: Any) -> Any:
    """创建或返回默认构建环境"""
    pass

def Dir(name: str) -> Any:
    """创建目录节点"""
    pass

def Export(*args: str, **kwargs: Any) -> None:
    """导出变量供其他构建脚本使用"""
    pass

def Import(*args: str) -> None:
    """从父脚本导入变量"""
    pass

def SConscript(scripts: str | List[str], **kwargs: Any) -> Any:
    """执行子构建脚本"""
    pass

def Default(target: Any) -> None:
    """设置默认构建目标"""
    pass

def Clean(target: Any, files: str | List[str]) -> None:
    """注册清理操作"""
    pass

def Help(text: str) -> None:
    """添加帮助信息"""
    pass
```

### 方法 2: 在文件开头添加注释
```python
# SConstruct
# SCons 内置函数参考：
# - DefaultEnvironment(**kwargs) -> Environment
# - Dir(name: str) -> Node
# - Export(*vars, **kw)
# - Import(*vars)
# - SConscript(scripts, **kw)
# - Default(targets)
# - Clean(target, files)
# - Help(text)

# 你的代码...
```

## 常用函数快速参考

| 函数 | 用途 | 示例 |
|------|------|------|
| `DefaultEnvironment()` | 获取默认环境 | `env = DefaultEnvironment()` |
| `Environment()` | 创建新环境 | `env = Environment(CC='gcc')` |
| `Dir(path)` | 获取目录节点 | `bin_dir = Dir('bin')` |
| `File(path)` | 获取文件节点 | `main_c = File('main.c')` |
| `Export(vars)` | 导出变量 | `Export('env')` |
| `Import(vars)` | 导入变量 | `Import('env')` |
| `SConscript(file)` | 执行子脚本 | `SConscript('src/SConscript')` |
| `Default(target)` | 设置默认目标 | `Default(program)` |
| `Clean(target, files)` | 清理文件 | `Clean('.', 'temp.txt')` |
| `Help(text)` | 添加帮助 | `Help('Custom help text')` |
| `Glob(pattern)` | 匹配文件 | `sources = Glob('*.c')` |
| `Depends(target, dep)` | 添加依赖 | `Depends(prog, config)` |
| `Alias(name, targets)` | 创建别名 | `Alias('install', install_files)` |

## 在线文档

- **SCons 官方文档**: https://scons.org/doc/production/HTML/scons-user.html
- **API 参考**: https://scons.org/doc/production/HTML/scons-api/
- **GitHub 源码**: https://github.com/SCons/scons

## 调试技巧

### 打印函数信息
```python
# 在 SConstruct 中
import inspect

env = DefaultEnvironment()
print("DefaultEnvironment 类型:", type(env))
print("DefaultEnvironment 位置:", inspect.getfile(type(env)))

# 查看环境的所有方法
print("可用方法:", [m for m in dir(env) if not m.startswith('_')])
```

### 查看 SCons 版本
```bash
scons --version
python3 -c "import SCons; print(SCons.__version__)"
```

### 启用调试输出
```bash
scons --debug=explain    # 解释为什么重新构建
scons --debug=tree       # 显示依赖树
scons -Q                 # 安静模式
scons -v                 # 详细模式
```

## 总结

1. **SCons 函数是注入的**：不是通过 import 导入，而是由 SCons 注入到执行环境
2. **源码在系统目录**：位于 `/usr/lib/python3/dist-packages/SCons/`
3. **IDE 支持有限**：可以通过 stub 文件或注释改善
4. **查阅官方文档**：最权威的函数说明
5. **直接看源码**：遇到疑问时查看源码最准确

---

**建议**：
- 新手先熟悉常用函数的用法
- 遇到问题优先查官方文档
- 需要深入理解时再查看源码
- 可以在项目中创建 stub 文件辅助开发
