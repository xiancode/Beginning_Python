#!/usr/bin/python
#-*-coding:utf-8-*-

#__metaclass__ = type  或者类为object的子类

class Rectangle(object):
	def __init__(self):
		self.width = 0
		self.height = 0
	def setSize(self,size):
		self.width,self.height = size
	def getSize(self):
		return self.width,self.height
	size = property(getSize,setSize)
	#size = property(getSize)  改成这种方式后，不能进行赋值


r = Rectangle()
r.width = 10
r.height = 5
print r.size
r.size = 150,100
print r.width
