# your code goes here
n1=int(input("enter the input")) 
upper=int(input("enter the input"))
for n in range(upper,n1):
	flag=0
	for i in range(2,n):
 		if n%i==0:
 			flag=1
 			break
	if flag==0:
		print(n)
		
