# intery point
import os
import re
goRepo = "cd e:/ws/navion-cartography"
bad_words = ("gag", "//debug")

data = os.popen(goRepo+ "& dir & git diff").read()

res = re.compile("diff \-\-git(.*)diff \-\-git")
v = res.search(data)

# data - raw str
# split diff by files
def getFileDiffs(data):
    strs = data.split('\n')
    newFile = ''
    res = []
    startDiff = False
    for str in strs:
        if "diff --git" in str:
            startDiff = True
            if newFile != '':
                res.append(newFile)
        if startDiff:
            newFile += str + "\n"
    res.append(newFile)
    return res

files = getFileDiffs(data)

badFiles = []
debugInfoExists = False
for file in files:
    strs = file.split('\n')
    for str in strs:
        for word in bad_words:
            if word in str:
                badFiles.append(strs[0])

if len(badFiles) != 0:
    print("ERROR! DEBUG INFO DETECTED!")
    for file in badFiles:
        print("See "+file)
else:
    print("Ok")