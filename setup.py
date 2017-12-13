import sys, os
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("GRARED.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = [],
        include_files = [],
        excludes = []
)


os.environ['TCL_LIBRARY'] = r'C:\Python35-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Python35-32\tcl\tk8.6'

setup(
    name = "GRARED",
    version = "0.5",
    description = "Gravimetric Data Reduction",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
