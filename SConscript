# -*- coding: utf-8 -*-

import os

# Import environment from SConstruct
Import('env', 'ROOT_DIR', 'SRC_DIR', 'BUILD_DIR', 'BIN_DIR', 'TARGET_NAME')

# Clone environment for local use
local_env = env.Clone()

# Collect source files
source_files = [
    'main.c',
]

# Convert to full paths
src_list = [os.path.join(SRC_DIR, f) for f in source_files]

# Compile source files to object files
objs = []
for src in src_list:
    obj = local_env.Object(src)
    objs.append(obj)

# Return object files
Return('objs')
