from cx_Freeze import setup, Executable
import sys
from os.path import join


include_files = [join('images'), join('audio'), join('src','sprites')]
build_exe_options= {"packages": ["pygame"], 'include_files': include_files,}


base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Space Shooter",
    version = "0.1",
    description = "Space Shooter Game",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py", base=base, icon=join('images', 'icon.ico'))]
)