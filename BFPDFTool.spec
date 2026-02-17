# -*- mode: python ; coding: utf-8 -*-

data = []
data.append(("y12.ico", "."))
data.append(("venv/Lib/site-packages/PySide6/translations", "PySide6/translations"))

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=data,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='BFPDFTool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['y12.ico'],
    contents_directory="."
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='BFPDFTool',
)
