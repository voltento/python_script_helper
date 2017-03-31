#platform=win
#args_count = 9
#rm alias for windows

import os, sys

if len(sys.argv) < 2:
    print("Wrong params...")
    exit(1)

args = ''
for arg in sys.argv[1:]:
    args += ' ' + arg

cmd = "DEL " + args

os.system(cmd)