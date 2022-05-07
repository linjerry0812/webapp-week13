from time import sleep
import sys
import os
import subprocess
import re
from random import randint
from copy import deepcopy
from os.path import exists

def expected():
    dat = [randint(1, 100) for _ in range(randint(5,15))]
    print(dat)
    idat = " ".join([str(_) for _ in dat])
    return idat, idat


def cleanup(s):
    r = s.strip()
    r = [" ".join(line.strip().split()) for line in r.split("\n")]
    return r


def failed(c, e):
    print(f"Your Output :\n{c}")
    print(f"Expected    :\n{e}")
    exit(1)


def test01(c, e):
    chk = cleanup(c)
    exp = cleanup(e)
    for a, b in zip(chk, exp):
        if a != b:
            failed(c, e)
    return c


def execMain(cmd, dat=""):
    dat = dat.encode('utf-8')
    p = subprocess.Popen([cmd, ],
                         shell=False,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE
                         )
    p.stdin.write(dat)
    output, error = p.communicate()
    output = output.decode('utf-8')
    p.stdin.close()
    return output


def main():
    root = f"./src/{sys.argv[0].split('_')[-1].split('.')[0]}"
    if sys.platform in ["win32"] and exists("main.cpp"):
        root = "."
    for i in range(10):
        dat, exp = expected()
        ret = test01(execMain(f'{root}/main', dat), exp)
    print("\n測試通過!")
    print(f"\n{ret}")
    exit(0)


if __name__ == "__main__":
    main()
