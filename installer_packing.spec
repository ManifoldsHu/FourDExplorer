# -*- mode: python ; coding: utf-8 -*-


block_cipher = None
py_files = [
    'FourDExplorer.py',
    'initial_config.py',
]

add_files = [
    ('ui\\resources\\icons\\*.png', 'ui\\resources\\icons'),
    ('ui\\resources\\images\\*.png', 'ui\\resources\\images'),
    ('ui\\resources\\themes\\dark\\*.xml', 'ui\\resources\\themes\\dark'),
    ('ui\\resources\\themes\\light\\*.xml', 'ui\\resources\\themes\\light')
]

a = Analysis(
    py_files,
    pathex=['.'],
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
    icon='ui\\resources\\icons\\4D.ico',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas, 
    strip=False,
    upx=True,
    upx_exclude=[],
    name='4D-Explorer',
)
