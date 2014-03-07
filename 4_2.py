#!/usr/bin/python
#coding=utf-8

labels = {
	'phone':'phone number',
	'addr' :'address'
}

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
name = raw_input('Name: ')

request = raw_input('Phone number (p) or address(a)?')

key = request
if request == 'p' : key = 'phone'
if request == 'a' : key = 'addresss'

person = people.get(name,{})
label = labels.get(key,key)
result = person.get(key,'not available')

print "%s's %s is %s," % (name,label,result)
