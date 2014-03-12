#!usr/bin/python
#-*- coding=utf-8 -*-
#cards.py

from pprint import pprint
from random import shuffle

values = range(1,11) + 'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['%s of %s ' %(v,s) for v in values for s in suits]

shuffle(deck)
print(deck[:12])
