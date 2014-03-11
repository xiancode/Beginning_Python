#!usr/bin/python
#-*-coding=utf-8-*-

#nested = [[[1,2],[2,4],[5]],[3,[4]]]
nested = [[['foo'],['bar','zoo']],['bar',['zip']]]

def flatten(nested):
	try:
	#不要迭代类似字符串的对象
		try: nested + ''
		except TypeError:pass
		else: raise TypeError
		for sublist in nested:
			for element in flatten(sublist):
				yield element
	except TypeError:
		yield nested

for num in flatten(nested):
	print num
