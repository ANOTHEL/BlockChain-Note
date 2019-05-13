import os
import shutil
import re
import sys

func = re.compile(".*func.*(.*).*{.*")

# /home/pilkyu/workspace/test/peer.go
def Main(file):
    print(file)
    f = open(file, "r")
    f1 = open("/home/pilkyu/workspace/test/peer1.go", "w")

    while 1:
        line = f.readline()

        if not line:
            break

        f1.writelines(line)

        if func.match(line):
            a = "    log.Info(\"[jpk] \") \n    log.Info(\"[jpk] \") \n    log.Info(\"[jpk] " + \
                line.strip() + "\") \n"            
            f1.writelines(a)
    f.close()
    os.remove(file)
    f1.close()
    shutil.move("/home/pilkyu/workspace/test/peer1.go",
                file)

if __name__ == "__main__":
    Main(sys.argv[1])
