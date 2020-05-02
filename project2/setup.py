import cx_Freeze
from cx_Freeze import *
import sys
cx_Freeze.setup(

    name="depart",
    version='0.01',
    description='for hse manager',
    options={'build_exe':{'packages':['tkinter','mysql']}},
    executables=[cx_Freeze.Executable("depart.py")

    ],
)
