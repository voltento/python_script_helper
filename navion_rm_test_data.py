#!/usr/bin/env python

import os
import shutil

repDir = "e:/ws/navion-cartography"

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def emoveTmpSubfolders(folder):
    dirs_row = get_immediate_subdirectories(folder)
    dirs = [ folder+'/'+ dir for dir in dirs_row if dir[0] is not '.']
    for dir in dirs:
        if dir.endswith("_tmp"):
            print("Remove ", dir)
            shutil.rmtree(dir)
        else:
            emoveTmpSubfolders(dir)

emoveTmpSubfolders(repDir)