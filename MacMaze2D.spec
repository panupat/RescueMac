# -*- mode: python -*-

block_cipher = None


a = Analysis(['MacMaze2D.py', 'constantes.py', 'labyManager.py', 'perso.py', 'position.py'],
             pathex=['/Users/panupat/development/github/RescueMac'],
             binaries=[],
             datas=[('maps/*', 'data'), ('images/*', 'data'), ('fonts/3270Medium.ttf', 'data')],
             hiddenimports=[],
             hookspath=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='MacMaze2D',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='MacMaze2D.app',
             icon=None,
             bundle_identifier=None)
