from parser import *
from node import *
from emit import *
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("latte: Error: Missing argument <input file>.")
        exit()

    prs = Prs(sys.argv[1])
    nodes = prs.prs()
    code = gen_node(nodes)

    with open("output.c", "w") as f:
        f.write(code)

    os.system("gcc -o output.exe output.c")