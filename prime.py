def isprimenumber(number):
    '''test if number is prime'''
    for x in range (1,number-1):
	print "x = ", x
	for y in range (x,number-1):
	    print "y = ", y
	    if x * y == number:
		return False
		break
    return True

def prime_range(start,end):
    '''print prime numbers in range'''
    totalnumbers = 0
    for x in range (start,end+1):
	num = isprimenumber(x)
	if num == True:
	    print x
	    totalnumbers = totalnumbers + 1
	#print "testing if %d is prime: %s"  % (x , isprimenumber(x) )
#	print isprimenumber(x)
    print "total prime numbers in range %d to %d : %d" % (start,end,totalnumbers)
	
print "testing for prime numbers in range " 
print prime_range(1,120)

