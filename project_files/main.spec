# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main.py'],
             pathex=[],
             binaries=[],
             datas=[('/Users/wishvapeiris/Desktop/FinalYearProject/venv/lib/python3.6/site-packages/eel/eel.js', 'eel'), ('web', 'web'), ('./config-file/yolov4-custom.cfg', 'config-file'), ('./frames', 'frames'), ('./test_videos/test6.mp4', 'test_videos'), ('./weights-file/yolov4-custom_3000.weights', 'weights-file'), ('./openCamera.py', '.'), ('./config.yaml', '.'), ('./upload.py', '.')],
             hiddenimports=['bottle_websocket'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
app = BUNDLE(coll,
             name='main.app',
             icon=None,
             bundle_identifier=None)
# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main.py'],
             pathex=[],
             binaries=[],
             datas=[('/Users/wishvapeiris/Desktop/FinalYearProject/venv/lib/python3.6/site-packages/eel/eel.js', 'eel'), ('web', 'web'), ('./config-file/yolov4-custom.cfg', 'config-file'), ('./frames', 'frames'), ('./test_videos/test6.mp4', 'test_videos'), ('./weights-file/yolov4-custom_3000.weights', 'weights-file'), ('./openCamera.py', '.'), ('./config.yaml', '.'), ('./upload.py', '.')],
             hiddenimports=['bottle_websocket'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
app = BUNDLE(coll,
             name='main.app',
             icon=None,
             bundle_identifier=None)
# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main.py'],
             pathex=[],
             binaries=[],
             datas=[('/Users/wishvapeiris/Desktop/FinalYearProject/venv/lib/python3.6/site-packages/eel/eel.js', 'eel'), ('web', 'web'), ('./config-file/yolov4-custom.cfg', 'config-file'), ('./frames', 'frames'), ('./test_videos/test6.mp4', 'test_videos'), ('./weights-file/yolov4-custom_3000.weights', 'weights-file'), ('./openCamera.py', '.'), ('./config.yaml', '.'), ('./upload.py', '.')],
             hiddenimports=['bottle_websocket'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
app = BUNDLE(coll,
             name='main.app',
             icon=None,
             bundle_identifier=None)
