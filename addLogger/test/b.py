import os
import shutil
import re
import sys

# /home/pilkyu/workspace/test/peer.go
# reIsFile = re.compile(".*\.")
reIsGo = re.compile(".*\.go")
isVendor = re.compile(".*vendor.*")
isTest = re.compile(".*test.*")
isBuild = re.compile(".*build.*")


def Main(path):
    if os.path.exists(path):
        print(path)
        print("path exist : " + path + '\n')

        if os.path.isdir(path) and not isVendor.match(path) and not isTest.match(path) and not isBuild.match(path):
            filenames = os.listdir(path)
            for file in filenames:
                Main(path + '/' + file)
            print(path)
            print("dir name is " + path)
            print('\n')
        elif reIsGo.match(path):
            print(path)
            print("go file name is " + path)
            print('\n')
            Transfer(path)
    else:
        print("no exist path : " + path + '\n')


func = re.compile("^func.*{$")
findLog = re.compile(".*/log\"$")


def Transfer(file):
    print(file)
    f = open(file, "r")
    tmpPath = file+".tmp"
    tmpFile = open(tmpPath, "w")

    while 1:
        print("while 1:")
        line = f.readline()
        print("line = f.readline()")
        check = False
        if line == "import (":
            check = True
        if check and findLog.match(line):
            check = True
        else:
            check = False

        if not line:
            print("if not line:")
            break
        print(line)

        if line == ")" and check:
            tmpFile.writelines("\"github.com/ethereum/go-ethereum/log \n\"")

        tmpFile.writelines(line)
        print("tmpFile.writelines(line)")

        if func.match(line):
            print("if func.match(line):")
            logLine = "    log.Info(\"[jpk] \") \n    log.Info(\"[jpk] \") \n    log.Info(\"[jpk] " + \
                line.strip() + "\") \n"
            tmpFile.writelines(logLine)
            print("????????????????????????????????????????????")
        else:
            print("else:")
    f.close()
    os.remove(file)
    tmpFile.close()
    shutil.move(tmpPath, file)


if __name__ == "__main__":
    Main(sys.argv[1])
