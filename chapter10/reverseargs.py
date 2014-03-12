#!usr/bin/python
#-*-coding=utf-8-*-
#reverseargs.py
import sys
args = sys.argv[1:]
args.reverse()
print ' '.join(args)
