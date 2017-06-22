n=int(input("enter the input"))
temp=n
rev=0
while temp!=0:
	rem=temp%10
	rev=rev*10+rem
	temp/=10
if rev==n:
	print('palin')
else:
	print('not a palin')
