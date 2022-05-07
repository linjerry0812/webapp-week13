from time import sleep
import sys
import subprocess
from random import randint
from os.path import exists
from copy import deepcopy


def index(dat):
    s = ""
    for i in range(10):
        if i in dat:
            s += f"{dat.index(i)} "
        else:
            s += "-1 "
    return s

def expected():
    dat = [randint(1, 15) for _ in range(randint(10,20))]
    idat = " ".join([str(_) for _ in dat])
    print(f"Test Data : {idat}")
    return idat, index(dat) 


def cleanup(s):
    r = s.strip()
    r = [line.strip() for line in r.split("\n")]
    noblk = []
    for l in r:
        if len(l) != 0:
            l = l.split()
            noblk.append([int(v) for v in l])
    return noblk


def failed(c, e):
    print(f"Your Output :\n{c}")
    print(f"Expected    :\n{e}")
    exit(1)


def test01(c, e):
    c = cleanup(c)[0]
    e = cleanup(e)[0]
    for a,b in zip(c,e):
        if a!=b: failed(c,e)
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
    print("\n測試通過!\n")
    for r in ret:
        print(f"{r}", end=" ")
    exit(0)


if __name__ == "__main__":
    main()