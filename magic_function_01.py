#!usr/bin/python
#-*-coding:utf-8-*-

def checkIndex(key):
	"""
	所给的键能接受索引吗?
	为了能被接受，键应该是一个非负的整数.
	如果不是一个整数会引起TypeError；
	如果是负数，则会引发IndexError.
	"""
	if not isinstance(key,(int,long)): raise TypeError
	if key < 0:
		raise IndexError


class ArithmeticSequence:
	def __init__(self,start=0,step=1):
		"""
		初始化算术序列
		初始值 - 序列中的第一个值
		步长 - 
		改变 - 用户修改的值的字典
		"""
		self.start = start  #保存开始值
		self.step = step    #保存步长值
		self.changed = {}   #没有项被修改
	def __getitem__(self,key):
		"""
		Get an item from the arithmetic sequence.
		"""
		checkIndex(key)
		try: return self.changed[key]              #修改了吗
		except KeyError:                           #否则
			return self.start + key*self.step  #.....计算值

	def __setitem__(self,key,value):
		"""
		修改一项的值
		"""
		checkIndex(key)
		self.changed[key] = value 


s = ArithmeticSequence(1,2)
print s[4]
s[4]=2
print s[4]
print s[5]
