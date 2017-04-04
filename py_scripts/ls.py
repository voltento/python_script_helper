#platform=win
#args_count = 9
# ls

from sys import platform
import sys
import os

cmd_args = ''
if len(sys.argv) > 1:
    for arg in sys.argv[:1]:
        cmd_args = arg + " "
cmd = ''
if platform == "linux" or platform == "linux2":
    cmd = 'ls ' + cmd_args
elif platform == "darwin":
    cmd = 'ls ' + cmd_args
elif platform == "win32":
    cmd = 'powershell ls ' + cmd_args
os.system(cmd)