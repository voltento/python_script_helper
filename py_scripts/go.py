#args_count = 1
# Opens addr from console in defoult brawser

import sys
import webbrowser
import os

if len(sys.argv) < 2:
    print("Wrong params. Exec ec. 'go www.google.ru', 'go gmail.com'")
    exit(1)

addr = sys.argv[1]
# chrome path different for different platforms
cmd = '"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe" ' + addr
os.system(cmd)