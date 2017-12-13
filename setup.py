import cx_Freeze
import os
import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from tkinter import *
from datetime import datetime
from math import sqrt, atan, asin, acos, sin, cos, radians



base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("GRARED.py", base=base, icon="clienticon.ico")]

os.environ['TCL_LIBRARY'] = r'C:\Python35-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Python35-32\tcl\tk8.6'

cx_Freeze.setup(
    name = "GRARED",
    options = {"build_exe": {"packages":["numpy","pandas","tkinter","datetime","math"], "include_files":["clienticon.ico"]}},
    version = "Alpha 0.5",
    description = "Gravimetric Data Reduction",
    executables = executables
    )
