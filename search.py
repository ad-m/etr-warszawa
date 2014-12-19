#!/usr/bin/env python3
from bs4 import BeautifulSoup
from sys import argv
for filename in argv[2:]:
    soup = BeautifulSoup(open(filename, "r"))
    for b in soup.findAll('tr'):
        if argv[1].lower() in b.text.lower():
#            import pdb;pdb.set_trace();
            text = b.text.replace("\n","\t")
            print(u"\033[1;36m%s\033[1;m: %s" % (filename, text))
