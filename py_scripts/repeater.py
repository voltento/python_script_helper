# Call command every n ms
# args: command -- native script, ms -- sleep time
import sys, time, os

if len(sys.argv) < 3:
    print ("Wrong params...")
    exit(1)

command = sys.argv[1]
ms = sys.argv[2]

while True:
    os.system(command)
    time.sleep(int(ms))
