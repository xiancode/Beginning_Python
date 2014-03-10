#!usr/bin/python
#coding=utf-8

#while True:
#	try:
#		x = input('Enter the first number:')
#		y = input('Enter the second number:')
#		value = x/y
#		print 'x/y is ',value
#	except Exception,e:
#		print 'Invalid input. ',e
#		print 'Please try again'
#	else:
#		break


def describePerson(person):
	print 'Description of ', person['name']
	print 'Age:',person['age']
	try:
		print 'Occupation:', person['occupation']
	except KeyError:
		print 'index error'

p = {'name':'pet','age':50,'work':'work'}


describePerson(p)
