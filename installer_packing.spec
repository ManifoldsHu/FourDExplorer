# -*- mode: python ; coding: utf-8 -*-

import os
import sys
import platform

# 获取系统架构和平台信息
bits, _ = platform.architecture()   # '64-bit', 'WindowsPE'
platform_os = sys.platform          # win32, darwin, linux

# 定义加密块为 None
block_cipher = None
py_files = [
    os.path.join('FourDExplorer', 'FourDExplorer.py'),
]

# 项目路径
project_path = os.getcwd()

# Python 主文件
py_files = [os.path.join('FourDExplorer', 'FourDExplorer.py')]

# 直接导入 Constants.py 获取 APP_VERSION
sys.path.insert(0, os.path.join(project_path, 'FourDExplorer'))
from Constants import APP_VERSION
print('APP_VERSION: {0}'.format(APP_VERSION))

# 打包名称
version = '.'.join([str(v) for v in APP_VERSION])
package_name = 'FourDExplorer-v{0}-{1}-{2}'.format(version, platform_os, bits)

# 需要额外包含的文件
add_files = [
    (os.path.join('FourDExplorer', 'ui', 'resources', 'icons', '*.png'), os.path.join('ui', 'resources', 'icons')),
    (os.path.join('FourDExplorer', 'ui', 'resources', 'icons', '*.ico'), os.path.join('ui', 'resources', 'icons')),
    (os.path.join('FourDExplorer', 'ui', 'resources', 'images', '*.png'), os.path.join('ui', 'resources', 'images')),
    (os.path.join('FourDExplorer', 'ui', 'resources', 'themes', 'dark', '*.xml'), os.path.join('ui', 'resources', 'themes', 'dark')),
    (os.path.join('FourDExplorer', 'ui', 'resources', 'themes', 'light', '*.xml'), os.path.join('ui', 'resources', 'themes', 'light'))
]

# 分析配置
a = Analysis(
    py_files,
    pathex=[os.path.join('.', 'FourDExplorer')],
    pathex=[os.path.join('.', 'FourDExplorer')],
    binaries=[],
    datas=add_files,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=True,  # 不生成单个可执行文件
)

# 打包 Python 代码
pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher,
)

# 创建可执行文件
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='4D-Explorer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=os.path.join('FourDExplorer', 'ui', 'resources', 'icons', '4D.ico'),
    icon=os.path.join('FourDExplorer', 'ui', 'resources', 'icons', '4D.ico'),
)

# 收集所有依赖和文件，生成目录结构
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=package_name,
)
