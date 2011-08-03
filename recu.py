def recufunc (x,y):
    if x < y:
	print "re1"
	return recufunc(x+1,y)
    else:
	return x
    
print recufunc(2,8)
print recufunc(1,20)
