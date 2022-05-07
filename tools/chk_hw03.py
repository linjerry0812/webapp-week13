from time import sleep
import sys
import os
import subprocess
import re
from random import randint
from os.path import exists


def expected():
    dat = [randint(1, 100) for _ in range(randint(5, 30))]
    idat = " ".join([str(_) for _ in dat])
    odat = "sum("
    if len(dat) > 10:
        odat += ",".join([str(_) for _ in dat[:10]])
        odat += f",...,{dat[-1]}) = {sum(dat)}"
    else:
        odat += ",".join([str(_) for _ in dat])
        odat += f") = {sum(dat)}"
    print(f"Test Data : {idat}")
    return idat, odat


def cleanup(s, eatspc=False):
    r = s.strip()
    r = [_ for _ in r.split("\n")]
    if eatspc:
        r = [oneSpc(_) for _ in r]
    return r


def oneSpc(s):
    s = s.strip()
    s = " ".join(s.split())
    return s


def failed(c, e):
    print(f"Your Output :\n{c}")
    print(f"Expected    :\n{e}")
    exit(1)


def test01(c, e):
    chk = cleanup(c, eatspc=True)
    exp = cleanup(e, eatspc=True)
    for a, b in zip(chk, exp):
        if a != b:
            failed(c, e)
    return c


def execMain(cmd, dat=""):
    dat = dat.encode('utf-8')
    p = subprocess.Popen(['node', cmd],
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
    if sys.platform in ["win32"] and exists("main.js"):
        root = "."
    # print(f'{root}/main')
    for i in range(10):
        dat, exp = expected()
        ret = test01(execMain(f'{root}/main.js', dat), exp)
    print("\n測試通過!")
    print(f"\n{ret}")
    exit(0)


if __name__ == "__main__":
    main()
