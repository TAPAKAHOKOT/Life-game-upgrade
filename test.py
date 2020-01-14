import subprocess
from multiprocessing import Process
import os


def fuct(num, name):
    global t
    t.hi()
    with open("test" + name + ".txt", "w") as f:
        for k in range(num):
            f.write("0")

        f.close()


class test:
    def __init__(self):
        print("ready")

    def hi(self):
        print(0)


global t
t = test()

if __name__ == '__main__':
    procs = []

    n = 4

    for k in range(n):
        proc = Process(target=fuct, args=(10**7 // n, str(k),))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
