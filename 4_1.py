#!/usr/bin/python
#coding=utf-8


people = {
	'Alice':{
		'phone':'2341',
		'addr' :'Foo driver 23'
		},

	'Beth':{
		'phone':'2333',
		'addr' :'doo triver 23'
		},
	'Cecil':{
		'phone':'3541',
		'addr' :'Baz driver 23'
		}
}

labels = {
	'phone':'phone number',
	'addr' :'address'
}

name = raw_input('Name: ')

request = raw_input('phone number(p) or address(a)?')

if request == 'p' : key = 'phone'
if request == 'a' : key = 'address'

if name in people : print "%s's %s,is %s" %  \
	(name,labels[key],people[name][key])
