#!usr/bin/python
#-*- coding=utf-8 -*-
#somescript.py

import sys
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print 'Wordcount:',wordcount
