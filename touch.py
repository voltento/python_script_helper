# args_count=9
import sys

print("len(sys.argv): "+str(len(sys.argv)))

if len(sys.argv) < 2:
    print("Wrong params. ex: 'touch.py file_name file_name2'")
    exit(1)

for file in sys.argv[1:]:
    open(file, 'a')
    print("Create file: "+ file)
                
