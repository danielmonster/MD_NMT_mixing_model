import os
import sys
from shutil import copyfile

# python copy_valid.py data-bin/expr10 10

directory = sys.argv[1] # "data-bin/expr10"
domain_nums = int(sys.argv[2])


valid1 = "valid.en-de.de.bin"
valid2 = "valid.en-de.de.idx"
valid3 = "valid.en-de.en.bin"
valid4 = "valid.en-de.en.idx"


for i in range(1, domain_nums):
    for valid in [valid1, valid2, valid3, valid4]:
        newv = valid[:5] + str(i) + valid[5:]
        copyfile(os.path.join(directory, valid), os.path.join(directory, newv))

