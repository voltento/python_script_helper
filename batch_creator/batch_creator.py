# Create batch wrapper on .py
# File .py have to include the line '#args_count=num' where num is num of arguments
#

import re, sys, os
import os

py_ext = ".py"
bat_ext = ".bat"

scripts_path = os.getcwd()+"/"
if len(sys.argv) == 2:
    scripts_path += sys.argv[1] + "/"	
else:
    scripts_path += "/../py_scripts/"	

out_path = os.getcwd() + "/../batch/"

if not os.path.exists(out_path):
    os.makedirs(out_path)

def getNumArgs(str):
    """
    Parse string '#args_count=num' return num
    :param str: String that look like '#args_count=num' where num is num of arguments
    :return: parsed num to int if succes else None
    """
    expr = re.compile("#\s*args_count\s*=\s*(\d+)\s*")
    res = expr.search(str)
    if res is None:
        return None
    return int(res.group(1))

def createBatchWrp(py_script_file, out_batch_file):
    """
    Create batch wrapper on python script
    :param py_script_file: path to file that will be wrapped
    :param out_batch_file: path to out batch file
    :return: None
    """
    python_interpret_command = "python "
    src = open(py_script_file, 'r')
    src.close()
    out = open(out_batch_file, 'w')
    out.write(python_interpret_command)
    out.write(py_script_file)
    numArgs = 9
    for i in range(1, numArgs+1):
        out.write(" %"+str(i))
    out.close()

def getPyScriptes(path):
    """
    Return list of .py scripts in path
    :param path: Path to scripts
    :return: list of .py script in path
    """
    files = []
    for file_name in os.listdir(path):
        if file_name.endswith(py_ext):
            files.append(file_name)
    return files

for file in getPyScriptes(scripts_path):
    createBatchWrp(scripts_path+file, out_path+file.replace(py_ext, bat_ext))
