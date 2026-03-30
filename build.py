import PyInstaller.__main__
import os

# Path to the main script
script_path = 'main.py'

# PyInstaller arguments
args = [
    script_path,
    '--onefile',
    '--windowed',
    '--name=PersonalFinanceManager',
    '--icon=icon.ico',  # Optional: add an icon if you have one
    '--add-data=transactions.json;.',  # Include the data file
    '--clean',
    '--noconfirm'
]

# Run PyInstaller
PyInstaller.__main__.run(args)

# Verify executable exists and check size
executable_name = "PersonalFinanceManager.exe"
executable_path = os.path.join("dist", executable_name)

if not os.path.exists(executable_path):
    raise FileNotFoundError(f"Executable not found at {executable_path}")

size_bytes = os.path.getsize(executable_path)
size_mb = size_bytes / (1024 * 1024)

print(f"Build complete. Executable size: {size_mb:.2f} MB")

if size_mb > 20:
    raise Exception(f"Executable size ({size_mb:.2f} MB) exceeds 20MB limit")

print(f"Executable verified at {executable_path}")