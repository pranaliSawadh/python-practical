def print_pattern(number):
	if number < 1 :
		return "enter number greater than or equals to 1"
	elif not number.is_integer():
		return "enter +ve integer value  greater than or equals to 1"  
	else :
		n = int(number)
		pattern = []
		for i in range(n*3):
			l = []
			for j in range(n*2+3):
				if(i==n and j==n+1):
					l.append(str(n))
					#print("*" ,end ="\n")
				
				elif i<=n and j<=n+1:
					if i+j==n+1:
						l.append("*")
						#print("*",end ="\n")
					else:
						l.append(" ")
						#print(" ",end ="")
				
				elif i>n and j<=n+1 and i<=n*2-1:
				#elif(n<i<2*n and n-1<j<=n):
					if i-j==n-1:
						l.append("*")
						#print("*",end ="\n")
					#print("*", end="")
					else:
						l.append(" ")
						#print(" ",end ="")
						
				elif i<=n and j>n+1:
					if j-i==n+1:
						l.append("*")
						#print("*",end ="\n")
					else:
						l.append(" ")
						#print(" " , end = "")
						
				elif i>n and j>n+1 and i<=n*2-1:
				#elif(n<i<2*n and n+1<j<=2*n):
					if i+j==n*3+1:
						l.append("*")
						#print("*", end = "\n")
					else:
						l.append(" ")
						#print(" ", end = "")
							
				elif(i>n*2-1):
					l.append("*")
					#print("*", end = "")
						
			pattern.append("".join(l))  
		return "\n".join(pattern)
					
print(print_pattern(4.0))
