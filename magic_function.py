#!/usr/bin/python
#coding=utf-8

__metaclass__ = type # super函数只在新式类中起作用
class Bird:
	def __init__(self):
		self.hungry = True
	def eat(self):
		if self.hungry:
			print 'Ahhhaa...'
			self.hungry = False
		else:
			print 'NO,thanks!'

class SongBird(Bird):
	def __init__(self):
		super(SongBird,self).__init__()
		self.sound = 'Squawk!'
	def sing(self):
		print self.sound

sb = SongBird()
sb.sing()

sb.eat()
sb.eat()
