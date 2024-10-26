# Auto_Job_Applier.spec

# Import necessary modules for the spec file
from PyInstaller.utils.hooks import collect_all

# Collect all files within the 'AUTO_JOB_APPLIER_LINKEDIN' folder
datas, binaries, hiddenimports = collect_all('AUTO_JOB_APPLIER_LINKEDIN')

# Define the PyInstaller configuration
a = Analysis(
    ['PyQt.py'],  # Specify the main script for the UI
    pathex=['.'],
    binaries=binaries,
    datas=datas + [
        ('all excels', 'AUTO_JOB_APPLIER_LINKEDIN/all excels'),  # Include CSVs in the bundle
        ('all resumes', 'AUTO_JOB_APPLIER_LINKEDIN/all resumes'),  # Include resume templates
        ('config', 'AUTO_JOB_APPLIER_LINKEDIN/config'),  # Include config files
        ('modules', 'AUTO_JOB_APPLIER_LINKEDIN/modules'),  # Include modules
        ('logs', 'AUTO_JOB_APPLIER_LINKEDIN/logs')  # Include logs folder
    ],
    hiddenimports=hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='AutoJobApplier',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    icon=None  # Optional: add path to an icon file if desired
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='AutoJobApplier'
)
