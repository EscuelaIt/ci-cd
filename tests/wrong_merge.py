import os
import sys


def test_wrong_merge():
    p = os.popen("grep -rnw ./djcourses -e \'<<<<<<< HEAD\'").read()
    if p:
        print(p)
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    test_wrong_merge()