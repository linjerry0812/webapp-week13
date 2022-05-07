from time import sleep
import sys
import os
import subprocess
import re

def expected():
    exp = '''
    gTime = 0,10,20,30,40,50,60,70,80,90,100
    gT1   = 125,106,184,53,31,168,183,69,199,102,50
    gT2   = 161,70,189,66,66,192,54,42,106,37,97
    gMemo = NA,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
    '''
    return "", exp


def cleanup(s):
    r = s.strip()
    r = [line.replace(' ', '') for line in r.split("\n")]
    return r


def failed(c, e):
    print(f"Your Output : {c}")
    print(f"Expected    : {e}")
    exit(1)


def test01(c, e):
    chk = cleanup(c)
    exp = cleanup(e)
    if chk[0] != exp[0]:
        failed(c, e)
    if chk[3] != exp[3]:
        failed(c, e)
    return c


def execMain(cmd,dat=""):
    p = subprocess.Popen(["node",cmd],
                         shell=False,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE
                         )
    p.stdin.write(b"100 10")
    output, error = p.communicate()
    output = output.decode('utf-8')
    p.stdin.close()
    return output


def main():
     # cwd = os.path.abspath(os.getcwd())
    dat, exp = expected()
    ret = test01(execMain('./src/lab02/main.js',dat), exp)
    print("測試通過!")
    print(f"\n{ret}")
    exit(0)


if __name__ == "__main__":
    main()
