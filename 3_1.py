#!/usr/bin/python
#coding=utf-8

width = input('Please enter width:')
price_width = 10
item_width = width - price_width

head_format = '%-*s%*s'
format      = '%-*s%*.2f'

print "="*width
print head_format % (item_width,'Item',price_width,'Price')

print '-'*width

print format % (item_width,'Apples',price_width,0.4)
print format % (item_width,'Pears',price_width,0.5)
print format % (item_width,'Cantaloupes',price_width,1.92)
print format % (item_width,'Deried Apricots(16)',price_width,8)
print format % (item_width,'Prunes (4 lbs.)',price_width,12)
