upper=100
low=1
for n in range(low,upper+1):
	for i in range(2,n):
 		if n%i==0:
 			break
	else:
			print n
		
