flag=0
n=int(input("enter the input"))
for i in range(2,n):
	if n%2==0:
		flag=1
if(flag==0):
	print '  is a prime'
else:
	print'  is not a prime'
