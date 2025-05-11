# -*- mode: python ; coding: utf-8 -*-

import os
import sys
import platform

# 获取系统信息
bits, _ = platform.architecture()
platform_os = sys.platform

# 定义项目路径和加密设置
project_path = os.getcwd()
block_cipher = None

# 导入版本信息
sys.path.insert(0, os.path.join(project_path, 'FourDExplorer'))
try:
    from Constants import APP_VERSION
    version = '.'.join([str(v) for v in APP_VERSION])
    package_name = f'FourDExplorer-v{version}'
    print(f'APP_VERSION: {version}')
except ImportError:
    constants_path = os.path.join(project_path, 'FourDExplorer', 'Constants.py')
    raise FileNotFoundError(f"Constants.py not found at {constants_path}")

# 定义资源文件路径
RESOURCES_BASE = os.path.join('FourDExplorer', 'ui', 'resources')
SCHEMA_BASE = os.path.join('FourDExplorer', 'schema')
MODELS_BASE = os.path.join('FourDExplorer', 'models')

# 组织资源文件
resource_files = [
    # UI 资源
    (os.path.join(RESOURCES_BASE, 'icons', '*.png'), os.path.join('ui', 'resources', 'icons')),
    (os.path.join(RESOURCES_BASE, 'icons', '*.ico'), os.path.join('ui', 'resources', 'icons')),
    (os.path.join(RESOURCES_BASE, 'images', '*.png'), os.path.join('ui', 'resources', 'images')),
    # 主题文件
    (os.path.join(RESOURCES_BASE, 'themes', 'dark', '*.xml'), os.path.join('ui', 'resources', 'themes', 'dark')),
    (os.path.join(RESOURCES_BASE, 'themes', 'light', '*.xml'), os.path.join('ui', 'resources', 'themes', 'light')),
    # 模式和模型文件
    (os.path.join(SCHEMA_BASE, 'MetaStructures', '*.json'), os.path.join('schema', 'MetaStructures')),
    (os.path.join(MODELS_BASE, '*.onnx'), os.path.join('models')),
]

# 模块文件
module_files = [
    (os.path.join('FourDExplorer', 'bin', '*'), 'bin'),
    (os.path.join('FourDExplorer', 'lib', '*'), 'lib'),
]

# 所有额外文件
add_files = resource_files + module_files

# 主执行文件
main_script = os.path.join('FourDExplorer', 'FourDExplorer.py')

# 必要的隐藏导入模块
hidden_imports = [
    'ipaddress',
    'encodings',
    'encodings.utf_8',
    'encodings.ascii',
    'encodings.latin_1',
]

# 排除的模块
excluded_modules = [
    'pkg_resources._vendor.jaraco.functools', 
    'pkg_resources._vendor.jaraco.context', 
    'pkg_resources._vendor.jaraco.text',
    'importlib_resources.trees',
    'PySide6.QtDBus'
]

# 图标路径
icon_path = os.path.join('FourDExplorer', 'ui', 'resources', 'icons', '4D.icns')

# 分析配置
a = Analysis(
    [main_script],
    pathex=[os.path.join(os.path.abspath('.'), 'FourDExplorer')],
    datas=add_files,
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=excluded_modules,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
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
    icon=icon_path,
)

# 根据平台创建最终的分发包
if platform_os == 'darwin':
    # macOS 应用捆绑包
    app = BUNDLE(
        exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        name=f'{package_name}.app',
        icon=icon_path,
        bundle_identifier='com.fourdstem.fourdexplorer',
        info_plist={
            'CFBundleShortVersionString': version,
            'NSHighResolutionCapable': 'True',
            'NSPrincipalClass': 'NSApplication',
            'NSAppleScriptEnabled': False,
        },
    )
else:
    # Windows/Linux 目录结构
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