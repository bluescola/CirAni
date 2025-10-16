#!/bin/bash
#
# 快速构建脚本
# 使用方法:
#   ./build.sh        - 编译项目
#   ./build.sh clean  - 清理
#   ./build.sh run    - 编译并运行
#

set -e  # 遇到错误立即退出

# 获取脚本所在目录（项目根目录）
PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$PROJECT_DIR"

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

function print_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

function print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

function print_warning() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

# 编译
function do_build() {
    print_info "开始编译..."
    scons -j4
    print_info "编译完成!"
}

# 清理
function do_clean() {
    print_info "清理构建文件..."
    scons -c
    rm -rf build bin
    print_info "清理完成!"
}

# 运行
function do_run() {
    BIN_PATH="$PROJECT_DIR/bin/CirAni"
    if [ ! -f "$BIN_PATH" ]; then
        print_error "可执行文件不存在，正在编译..."
        do_build
    fi

    print_info "运行程序..."
    "$BIN_PATH"
}

# 编译并运行
function do_build_and_run() {
    do_build
    do_run
}

# 显示帮助
function show_help() {
    cat << EOF
========================================
CirAni 快速构建脚本
========================================

使用方法:
  ./build.sh [命令]

命令:
  (无)      - 编译项目
  clean     - 清理构建文件
  run       - 运行程序
  br        - 编译并运行
  help      - 显示此帮助

示例:
  ./build.sh          # 编译
  ./build.sh clean    # 清理
  ./build.sh br       # 编译并运行

========================================
EOF
}

# 主逻辑
case "${1:-build}" in
    build)
        do_build
        ;;
    clean)
        do_clean
        ;;
    run)
        do_run
        ;;
    br|build-run)
        do_build_and_run
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        print_error "未知命令: $1"
        show_help
        exit 1
        ;;
esac
