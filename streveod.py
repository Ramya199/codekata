str=raw_input("enter the string")
for i in range (len(str)):
	tmp = str[i]
	str[i] = str[i+1] 
	str[i+1] = tmp
	print str
