database = [
	['albert','1234'],
	['dilbert',4242],
	['smith',7524],
	['jones',9843]
]

username = raw_input('user name:')
pin = raw_input('Pin code:')

if[username,pin] in database:print 'Access granted'
