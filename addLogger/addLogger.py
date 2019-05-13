import os
import shutil
import re
import sys

reIsGo = re.compile(".*\.go")
isVendor = re.compile(".*vendor.*")
isTest = re.compile(".*test.*")
isBuild = re.compile(".*build.*")
isSwarm = re.compile(".*swarm.*")
isCrypto = re.compile(".*crypto.*")
isParams = re.compile(".*params.*")
isCommon = re.compile(".*common.*")
isRlp = re.compile(".*rlp.*")
isUtils = re.compile(".*utils.*")
isLog = re.compile(".*log.*")
isMetrics = re.compile(".*metrics.*")
isBind = re.compile(".*bind.*")
isContract = re.compile(".*contract.*")
isMobile = re.compile(".*mobile.*")
isEnode = re.compile(".*enode.*")
isEnr = re.compile(".*enr.*")
# isTrie = re.compile(".*trie.*")
# isTypes = re.compile(".*types.*")
# isEthDb = re.compile(".*ethdb.*")


def Main(path):
    if os.path.exists(path):
        # print(path)
        # print("path exist : " + path + '\n')

        if os.path.isdir(path) and not isVendor.match(path) and not isTest.match(path) and not isBuild.match(path) and not isCrypto.match(path) and not isLog.match(path) and not isSwarm.match(path) and not isMetrics.match(path) and not isBind.match(path) and not isContract.match(path) and not isMobile.match(path) and not isRlp.match(path) and not isUtils.match(path) and not isParams.match(path) and not isCommon.match(path) and not isEnode.match(path) and not isEnr.match(path):
            # and not isTypes.match(path)  and not isTrie.match(path) and not isEthDb.match(path):
            filenames = os.listdir(path)
            for file in filenames:
                Main(path + '/' + file)
            # print(path)
            # print("dir name is " + path)
            # print('\n')
        elif reIsGo.match(path):
            print(path)
            print("go file name is " + path)
            print('\n')
            if fileOpen(path):
                addLog(path)
    # else:
        # print("no exist path : " + path + '\n')


func = re.compile("^func.*\{$")
findLog = re.compile(".*/log\"$")


def fileOpen(file):
    filePoint = open(file, "r")
    lines = filePoint.readlines()
    for line in(lines):
        if func.match(line):
            filePoint.close()
            return True


def addLog(file):
    print("file name is" + file)
    f = open(file, "r")
    tmpPath = file+".tmp"
    tmpFile = open(tmpPath, "w")

    check = False
    printLog = False

    while 1:
        # print("while 1:")
        line = f.readline()
        # print("line = f.readline()")

        if line.strip() == "import (":
            # print("if line == \"import (\":")
            check = True

        if findLog.match(line):
            # print("if check ansd findLog.match(line):")
            check = False

        if not line:
            # print("if not line:")
            break
        # print(line)

        if line.strip() == ")" and check:
            # print("if line == \")\" and check:")
            logPath = "    \"github.com/ethereum/go-ethereum/log\"" + "\n"
            tmpFile.writelines(logPath)
            check = False
            printLog = True
        # else:
            # print(line.strip())
            # print(check)

        tmpFile.writelines(line)
        # print("tmpFile.writelines(line)")

        if func.match(line) and printLog:
            # print("if func.match(line):")
            logLine = "    log.Info(\"[jpk] \") \n    log.Info(\"[jpk] \") \n    log.Info(\"[jpk] " + \
                line.strip() + "\") \n"
            tmpFile.writelines(logLine)
        # else:
        #     check = False
    f.close()
    os.remove(file)
    tmpFile.close()
    shutil.move(tmpPath, file)


if __name__ == "__main__":
    Main(sys.argv[1])
