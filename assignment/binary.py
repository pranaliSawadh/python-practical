def binary_subtraction(num1 , num2):
	#binary representation of the given numbers
	bin1 = toBinary(num1)
	bin2 = toBinary(num2)
	
	#make length of both binary numbers equall by adding leading zeroes to shorter one
	max_len = max(len(bin1),len(bin2))
	bin1 = bin1.zfill(max_len)
	bin2 = bin2.zfill(max_len)
	
	#print(bin1,bin2)
	result = ""
	borrow = 0
	
	#Traverse both the string from right to left
	for i,j in zip(reversed(bin1),reversed(bin2)):
		b1 = int(i)	#bit from bin1
		b2 = int(j)	#bit from bin2
		
		#handle borrow if there is any borrow from previous bit 
		b1-=borrow
		
		if b1<b2:
			b1+=2	#borrow is necessary
			borrow = 1
		else:
			borrow = 0
			
		result = str(b1-b2)+result  #perform actual subtraction and add it to result
	result = result.lstrip("0")	#removes unnecessary zeroes 
	
	#return "0" if result is empty otherwise print result of subtraction
	if result=="":
		return "0"
	else:
		return "subtraction of " + bin1+" and " +bin2+ " is " + result
	
#function to convert decimal to binary
def toBinary(n):
	if n==0:
		return "0"
	l = []
	while n>0:
		#if remainder of n when divided by 2 is 0 return 0
		if n%2==0:
			l.append(0)
		#if remainder of n when divided by 2 is 1 return 1
		elif n%2!=0:
			l.append(1)
		
		n//=2	#divide n by 2 and return n to the while loop
	l.reverse()
	s = "".join(map(str,l))	
	return s

print(binary_subtraction(10,4))
print(binary_subtraction(8,4))
print(binary_subtraction(20,10))

