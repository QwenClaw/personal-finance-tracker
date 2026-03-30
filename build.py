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

print("Build complete. Executable should be in the 'dist' folder.")