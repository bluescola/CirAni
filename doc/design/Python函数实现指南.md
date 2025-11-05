# Python 配置管理函数实现指南

## 文档说明

本文档列出实现 CirAni 配置管理功能所需的所有 Python 函数及其用法示例。

---

## 一、文件和目录操作

### 1.1 路径操作

#### `os.path.join(path1, path2, ...)`
**功能**: 智能拼接路径（自动处理不同操作系统的路径分隔符）

**示例**:
```python
import os

root = '/home/zane/project/raylib_pro/CirAni'
config_path = os.path.join(root, 'target', 'configs')
# 结果: '/home/zane/project/raylib_pro/CirAni/target/configs'

config_file = os.path.join(root, '.config')
# 结果: '/home/zane/project/raylib_pro/CirAni/.config'
```

**用途**:
- 构建配置文件路径
- 构建配置目录路径

---

#### `os.path.exists(path)`
**功能**: 检查文件或目录是否存在

**示例**:
```python
config_file = '/home/zane/project/raylib_pro/CirAni/.config'

if os.path.exists(config_file):
    print("配置文件存在")
else:
    print("配置文件不存在")
```

**返回值**: `True` 或 `False`

**用途**:
- 检查配置文件是否存在
- 检查配置目录是否存在

---

#### `os.path.dirname(path)`
**功能**: 获取文件的父目录路径

**示例**:
```python
file_path = '/home/zane/project/file.txt'
parent_dir = os.path.dirname(file_path)
# 结果: '/home/zane/project'
```

---

### 1.2 目录操作

#### `os.listdir(path)`
**功能**: 列出目录中的所有文件和子目录

**示例**:
```python
configs_dir = '/home/zane/project/raylib_pro/CirAni/target/configs'

files = os.listdir(configs_dir)
# 结果: ['desktop_linux_basic_defconfig', 'desktop_linux_advanced_defconfig', ...]

# 遍历文件
for filename in files:
    print(filename)
```

**用途**:
- 列出所有配置文件

---

### 1.3 文件操作

#### `open(file, mode)` + `with`
**功能**: 打开文件（推荐使用 with 语句自动关闭）

**模式**:
- `'r'`: 只读
- `'w'`: 写入（覆盖）
- `'a'`: 追加

**示例**:
```python
# 读取文件
with open('/path/to/file.txt', 'r') as f:
    content = f.read()  # 读取全部内容

# 逐行读取
with open('/path/to/file.txt', 'r') as f:
    for line in f:
        print(line)

# 写入文件
with open('/path/to/file.txt', 'w') as f:
    f.write('Hello World\n')
```

**用途**:
- 读取 `.config` 文件
- 写入 `.defconfig` 标记文件

---

#### `shutil.copy(src, dst)`
**功能**: 复制文件

**示例**:
```python
import shutil

src = '/home/zane/project/target/configs/desktop_linux_basic_defconfig'
dst = '/home/zane/project/.config'

shutil.copy(src, dst)
# 将 src 复制到 dst
```

**用途**:
- 应用配置（复制 defconfig 到 .config）
- 保存配置（复制 .config 到 defconfig）

---

## 二、字符串操作

### 2.1 基础操作

#### `str.strip([chars])`
**功能**: 去除字符串首尾的空白字符（空格、换行、制表符）

**示例**:
```python
line = "  CONFIG_PRJ_TARGET=\"desktop_linux\"  \n"
line = line.strip()
# 结果: "CONFIG_PRJ_TARGET=\"desktop_linux\""

# 去除特定字符
text = "___hello___"
text = text.strip('_')
# 结果: "hello"
```

**用途**:
- 处理配置文件的每一行

---

#### `str.split(separator, maxsplit=-1)`
**功能**: 按分隔符分割字符串

**示例**:
```python
line = "CONFIG_PRJ_TARGET=\"desktop_linux\""

# 分割一次
key, value = line.split('=', 1)
# key = "CONFIG_PRJ_TARGET"
# value = "\"desktop_linux\""

# 分割多次
text = "a,b,c,d"
parts = text.split(',')
# 结果: ['a', 'b', 'c', 'd']
```

**参数**:
- `separator`: 分隔符
- `maxsplit`: 最多分割次数（1 表示只分割第一个）

**用途**:
- 解析 `KEY=VALUE` 格式

---

#### `str.startswith(prefix)` / `str.endswith(suffix)`
**功能**: 检查字符串是否以指定前缀/后缀开头/结尾

**示例**:
```python
line = "# 这是注释"
if line.startswith('#'):
    print("这是注释行")

filename = "desktop_linux_basic_defconfig"
if filename.endswith('_defconfig'):
    print("这是配置文件")
```

**用途**:
- 跳过注释行
- 过滤配置文件

---

#### `str.replace(old, new)`
**功能**: 替换字符串中的内容

**示例**:
```python
filename = "desktop_linux_basic_defconfig"
config_name = filename.replace('_defconfig', '')
# 结果: "desktop_linux_basic"

text = "\"desktop_linux\""
text = text.replace('"', '')
# 结果: "desktop_linux"
```

**用途**:
- 去除配置文件名的后缀
- 去除引号

---

#### 字符串切片 `str[start:end]`
**功能**: 提取字符串的一部分

**示例**:
```python
text = "\"desktop_linux\""

# 去掉首尾字符
result = text[1:-1]
# 结果: "desktop_linux"

# 从开头提取
text = "hello world"
result = text[:5]
# 结果: "hello"

# 从指定位置到末尾
result = text[6:]
# 结果: "world"
```

**用途**:
- 去除引号

---

### 2.2 格式化输出

#### f-string (推荐)
**功能**: 格式化字符串（Python 3.6+）

**示例**:
```python
name = "CirAni"
version = "1.0"

# 基础用法
msg = f"项目名称: {name}, 版本: {version}"
# 结果: "项目名称: CirAni, 版本: 1.0"

# 对齐
text = f"{'左对齐':<10}|{'右对齐':>10}|{'居中':^10}"
# 结果: "左对齐        |      右对齐|    居中    "

# 指定宽度
desc = "配置文件"
value = "desktop_linux"
line = f"  {desc:12s} : {value}"
# 结果: "  配置文件     : desktop_linux"
```

**用途**:
- 格式化输出配置信息
- 美化打印

---

#### `str.format()`
**功能**: 格式化字符串（旧版方式）

**示例**:
```python
msg = "项目: {}, 版本: {}".format("CirAni", "1.0")
# 结果: "项目: CirAni, 版本: 1.0"

msg = "项目: {name}, 版本: {ver}".format(name="CirAni", ver="1.0")
```

---

## 三、列表操作

### 3.1 创建和添加

#### 创建列表
```python
# 空列表
configs = []

# 有初始值的列表
configs = ['config1', 'config2']
```

#### `list.append(item)`
**功能**: 在列表末尾添加元素

**示例**:
```python
configs = []
configs.append('desktop_linux_basic_defconfig')
configs.append('desktop_linux_advanced_defconfig')
# 结果: ['desktop_linux_basic_defconfig', 'desktop_linux_advanced_defconfig']
```

**用途**:
- 收集配置文件名

---

### 3.2 排序

#### `list.sort()`
**功能**: 对列表进行原地排序

**示例**:
```python
configs = ['c_defconfig', 'a_defconfig', 'b_defconfig']
configs.sort()
# 结果: ['a_defconfig', 'b_defconfig', 'c_defconfig']

# 倒序
configs.sort(reverse=True)
```

**用途**:
- 排序配置文件列表

---

### 3.3 遍历

#### `for ... in ...`
```python
configs = ['config1', 'config2', 'config3']

# 方式1: 只遍历值
for config in configs:
    print(config)

# 方式2: 遍历索引和值
for i, config in enumerate(configs):
    print(f"{i}. {config}")
# 输出:
# 0. config1
# 1. config2
# 2. config3

# 从1开始编号
for i, config in enumerate(configs, 1):
    print(f"{i}. {config}")
# 输出:
# 1. config1
# 2. config2
# 3. config3
```

**用途**:
- 遍历配置文件列表并编号

---

## 四、字典操作

### 4.1 创建和添加

#### 创建字典
```python
# 空字典
config_dict = {}

# 有初始值的字典
config_dict = {
    'CONFIG_PRJ_TARGET': 'desktop_linux',
    'CONFIG_PRJ_APP': 'basic_circuit'
}
```

#### 添加键值对
```python
config_dict = {}
config_dict['CONFIG_PRJ_TARGET'] = 'desktop_linux'
config_dict['CONFIG_PRJ_APP'] = 'basic_circuit'
```

**用途**:
- 存储配置项

---

### 4.2 获取值

#### `dict.get(key, default=None)`
**功能**: 获取字典中的值（推荐，不会报错）

**示例**:
```python
config = {
    'CONFIG_PRJ_TARGET': 'desktop_linux',
    'CONFIG_PRJ_APP': 'basic_circuit'
}

# 获取存在的键
target = config.get('CONFIG_PRJ_TARGET')
# 结果: 'desktop_linux'

# 获取不存在的键（返回默认值）
width = config.get('CONFIG_SCREEN_WIDTH', '800')
# 结果: '800'

# 如果不设置默认值，返回 None
value = config.get('NOT_EXIST')
# 结果: None
```

**用途**:
- 安全地获取配置值

---

#### 直接访问 `dict[key]`
```python
config = {'CONFIG_PRJ_TARGET': 'desktop_linux'}

target = config['CONFIG_PRJ_TARGET']
# 结果: 'desktop_linux'

# 注意：如果键不存在会报错
value = config['NOT_EXIST']  # ❌ KeyError
```

---

### 4.3 遍历

#### `dict.items()`
**功能**: 遍历字典的键值对

**示例**:
```python
config = {
    'CONFIG_PRJ_TARGET': 'desktop_linux',
    'CONFIG_PRJ_APP': 'basic_circuit',
    'CONFIG_SCREEN_WIDTH': '800'
}

# 遍历键值对
for key, value in config.items():
    print(f"{key} = {value}")
# 输出:
# CONFIG_PRJ_TARGET = desktop_linux
# CONFIG_PRJ_APP = basic_circuit
# CONFIG_SCREEN_WIDTH = 800
```

**用途**:
- 遍历配置字典

---

#### `dict.keys()` / `dict.values()`
```python
# 只遍历键
for key in config.keys():
    print(key)

# 只遍历值
for value in config.values():
    print(value)
```

---

### 4.4 检查键是否存在

#### `key in dict`
```python
config = {'CONFIG_PRJ_TARGET': 'desktop_linux'}

if 'CONFIG_PRJ_TARGET' in config:
    print("目标平台已配置")
```

---

## 五、异常处理

### `try-except`
**功能**: 捕获并处理异常

**示例**:
```python
try:
    # 尝试执行的代码
    with open('file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    # 文件不存在时执行
    print("文件不存在")
except Exception as e:
    # 其他所有异常
    print(f"发生错误: {e}")
```

**用途**:
- 处理文件操作可能的错误

---

## 六、实战示例

### 示例 1: 实现 `list_defconfig(root)`

```python
def list_defconfig(root):
    """列出所有可用的配置文件"""

    # 1. 构建配置目录路径
    configs_path = os.path.join(root, 'target', 'configs')

    # 2. 检查目录是否存在
    if not os.path.exists(configs_path):
        pr_err("配置目录不存在")
        return []

    # 3. 创建空列表存储配置文件名
    configs = []

    # 4. 遍历目录
    for filename in os.listdir(configs_path):
        # 5. 只收集以 _defconfig 结尾的文件
        if filename.endswith('_defconfig'):
            configs.append(filename)

    # 6. 排序
    configs.sort()

    # 7. 格式化输出
    if configs:
        print("\n" + "="*60)
        print("可用的配置文件:")
        print("="*60)
        for i, cfg in enumerate(configs, 1):
            print(f"  {i}. {cfg}")
        print("="*60 + "\n")
    else:
        print("没有找到配置文件")

    # 8. 返回列表
    return configs
```

**用到的函数**:
- `os.path.join()` - 拼接路径
- `os.path.exists()` - 检查目录
- `os.listdir()` - 列出文件
- `str.endswith()` - 过滤文件
- `list.append()` - 添加到列表
- `list.sort()` - 排序
- `enumerate()` - 遍历并编号

---

### 示例 2: 实现 `get_all_config(root)`

```python
def get_all_config(root):
    """读取 .config 文件的所有配置项"""

    # 1. 构建配置文件路径
    config_file = os.path.join(root, '.config')

    # 2. 检查文件是否存在
    if not os.path.exists(config_file):
        pr_warn("配置文件不存在")
        return {}

    # 3. 创建空字典
    config_dict = {}

    # 4. 使用 try-except 处理可能的错误
    try:
        # 5. 打开文件
        with open(config_file, 'r') as f:
            # 6. 逐行读取
            for line in f:
                # 7. 去除首尾空白
                line = line.strip()

                # 8. 跳过空行
                if not line:
                    continue

                # 9. 跳过注释行
                if line.startswith('#'):
                    continue

                # 10. 解析 KEY=VALUE
                if '=' in line:
                    # 11. 分割字符串
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip()

                    # 12. 去除引号
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]

                    # 13. 存入字典
                    config_dict[key] = value

        # 14. 返回字典
        return config_dict

    except Exception as e:
        pr_err(f"读取配置文件失败: {e}")
        return {}
```

**用到的函数**:
- `os.path.join()` - 拼接路径
- `os.path.exists()` - 检查文件
- `open()` + `with` - 打开文件
- `str.strip()` - 去除空白
- `str.startswith()` - 检查前缀
- `str.split()` - 分割字符串
- 字符串切片 `[1:-1]` - 去除引号
- `dict[key] = value` - 存入字典
- `try-except` - 异常处理

---

### 示例 3: 实现 `apply_defconfig(root, defconfig_name)`

```python
def apply_defconfig(root, defconfig_name):
    """应用指定的配置文件"""

    # 1. 构建源文件路径
    src = os.path.join(root, 'target', 'configs', defconfig_name)

    # 2. 检查源文件是否存在
    if not os.path.exists(src):
        pr_err(f"配置文件不存在: {defconfig_name}")
        return False

    # 3. 构建目标文件路径
    dst = os.path.join(root, '.config')

    # 4. 使用 try-except 处理错误
    try:
        # 5. 导入 shutil 模块
        import shutil

        # 6. 复制文件
        shutil.copy(src, dst)

        # 7. 创建 .defconfig 标记文件
        marker_file = os.path.join(root, '.defconfig')
        with open(marker_file, 'w') as f:
            # 8. 去掉 _defconfig 后缀
            config_name = defconfig_name.replace('_defconfig', '')
            f.write(config_name)

        # 9. 输出成功信息
        pi(f"已应用配置: {defconfig_name}")
        return True

    except Exception as e:
        pr_err(f"应用配置失败: {e}")
        return False
```

**用到的函数**:
- `os.path.join()` - 拼接路径
- `os.path.exists()` - 检查文件
- `shutil.copy()` - 复制文件
- `open()` + `with` - 写入文件
- `str.replace()` - 替换字符串
- `try-except` - 异常处理

---

## 七、常用导入语句

```python
import os          # 文件和目录操作
import sys         # 系统相关
import shutil      # 高级文件操作（复制、移动等）
```

---

## 八、快速查找表

| 需求 | 使用的函数 |
|------|-----------|
| 拼接路径 | `os.path.join()` |
| 检查文件/目录是否存在 | `os.path.exists()` |
| 列出目录内容 | `os.listdir()` |
| 读取文件 | `open()` + `with` |
| 复制文件 | `shutil.copy()` |
| 去除空白 | `str.strip()` |
| 分割字符串 | `str.split()` |
| 检查前缀/后缀 | `str.startswith()` / `str.endswith()` |
| 替换字符串 | `str.replace()` |
| 字符串切片 | `str[start:end]` |
| 格式化字符串 | f-string: `f"{变量}"` |
| 列表添加元素 | `list.append()` |
| 列表排序 | `list.sort()` |
| 字典存值 | `dict[key] = value` |
| 字典取值 | `dict.get(key, default)` |
| 遍历字典 | `for k, v in dict.items():` |
| 异常处理 | `try-except` |

---

## 九、调试技巧

### 打印调试信息
```python
# 打印变量
print(f"变量值: {variable}")

# 打印类型
print(f"类型: {type(variable)}")

# 打印长度
print(f"长度: {len(list_or_dict)}")

# 打印所有内容
print(f"内容: {variable}")
```

### 检查路径
```python
path = "/some/path"
print(f"路径: {path}")
print(f"存在: {os.path.exists(path)}")
print(f"是文件: {os.path.isfile(path)}")
print(f"是目录: {os.path.isdir(path)}")
```

---

## 十、参考资料

### 函数实现顺序建议

1. **先实现** `get_all_config()` - 基础函数，其他函数会用到
2. **再实现** `list_defconfig()` - 最简单，练手
3. **然后** `apply_defconfig()` - 涉及文件复制
4. **接着** `show_defconfig_info()` - 用到 `get_all_config()`
5. **最后** `save_defconfig()` - 综合运用前面的函数

---

**文档版本**: v1.0
**创建日期**: 2025-01-05
**维护者**: CirAni Team
