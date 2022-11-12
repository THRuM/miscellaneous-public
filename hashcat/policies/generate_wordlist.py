#!/usr/bin/python

import os
import sys

source_file = sys.argv[1]
destination_file = sys.argv[2]

mask_file = open(source_file, 'r')
lines = mask_file.readlines()

special_characters = "\!\@#$%\&+"

for line in lines:
    #print("mp64 %s -o %s" % (line.strip(), destination_file))
    os.system("mp64 %s -o %s --custom-charset1=%s" % (line.strip(), destination_file, special_characters))

