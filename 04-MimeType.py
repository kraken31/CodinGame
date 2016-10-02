import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

table = {}

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    table[ext.lower()] = mt
    
for i in range(q):
    fname = input()  # One file name per line.
    extension = ""
    if fname.find(".") >= 0:
        extension = fname[fname.rfind(".")+1:]
        if extension.lower() in table:
            print(table[extension.lower()])
        else:
            print("UNKNOWN")
    else:
        print("UNKNOWN")