#args_count = 1
# Start pydoc info by arg or pydoc server if args num equal 0

import sys, os
from os import path

pydoc_path = "/lib/pydoc.py"
python_path = os.path.split(sys.executable)[0]
pydoc_full_path = python_path + pydoc_path
arg = "-b"

if len(sys.argv) >= 2:
    arg = sys.argv[1]
os.system("python " + pydoc_full_path + " "+arg)