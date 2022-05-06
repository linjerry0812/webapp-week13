from time import sleep
import sys
import os
import subprocess
import re

def expected():
    return "","Hello STUST!"


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
    return c


def execMain(cmd,dat=""):
    p = subprocess.Popen(["node",cmd],
                         shell=False,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE
                         )
    output, error = p.communicate()
    output = output.decode('utf-8')
    p.stdin.close()
    return output


def main():
    global expected
    # cwd = os.path.abspath(os.getcwd())
    dat, exp = expected()
    ret = test01(execMain('./src/lab01/main.js',dat), exp)
    print("測試通過!")
    print(f"\n{ret}")
    exit(0)


if __name__ == "__main__":
    main()
