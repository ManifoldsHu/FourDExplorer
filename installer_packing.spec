# -*- mode: python ; coding: utf-8 -*-

import platform 
import sys
import os 

bits, _ = platform.architecture()   # '64-bit', 'WindowsPE'
platform_os = sys.platform          # win32

block_cipher = None
py_files = [
    'FourDExplorer\\FourDExplorer.py',
]

# Read APP_VERSION variable from Constants.py file
with open(os.path.join(os.getcwd(), 'FourDExplorer', 'Constants.py'), encoding='utf-8') as f:
    try:
        exec(f.read())
    except NameError:
        pass 
    finally:
        print('APP_VERSION: {0}'.format(APP_VERSION))
version = '.'.join([str(v) for v in APP_VERSION])

package_name = 'FourDExplorer-v{0}-{1}-{2}'.format(version, platform_os, bits)

add_files = [
    ('FourDExplorer\\ui\\resources\\icons\\*.png', 'ui\\resources\\icons'),
    ('FourDExplorer\\ui\\resources\\icons\\*.ico', 'ui\\resources\\icons'),
    ('FourDExplorer\\ui\\resources\\images\\*.png', 'ui\\resources\\images'),
    ('FourDExplorer\\ui\\resources\\themes\\dark\\*.xml', 'ui\\resources\\themes\\dark'),
    ('FourDExplorer\\ui\\resources\\themes\\light\\*.xml', 'ui\\resources\\themes\\light')
]

a = Analysis(
    py_files,
    pathex=['.\\FourDExplorer\\'],
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
    noarchive=False,
)

pyz = PYZ(
    a.pure, 
    a.zipped_data,   
    cipher=block_cipher,
)

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
    icon='FourDExplorer\\ui\\resources\\icons\\4D.ico',
)

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
