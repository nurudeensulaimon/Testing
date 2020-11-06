def repeat(object, times=None):
	#repeat (10,3) --> 10, 10, 10
	if times is None:
		while True:
			yield object 
	else:
		for i in xrange(times):
			yield object 


stest = repeat(10)
print(stest)
