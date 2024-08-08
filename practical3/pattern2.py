def pattern(len):
		pattern = []
		for i in range(len*2+1):
			line = []
			for j in range(len*2+3):
				if i<=len and j<=len+1: 
					if i+j==len+1:
						line.append("+")
					else:
						line.append(" ")
				elif i>len and j<=len+1 and i<=len*2-1:
					if i-j==len-1:
						line.append("+")
					else:
						line.append(" ")
				elif i<=len and j>len+1:
					if j-i==len+1:
						line.append("+")
					else:
						line.append(" ")
				elif i>len and j>len+1 and i<=len*2:
					if i+j==len*3+1:
						line.append("+")
					else:
						line.append(" ")
						
				elif i==len*2 and j==len:
					line.append(" -")
				else:
					line.append(" ")		
			pattern.append("".join(line))  
		return "\n".join(pattern)
		
print(pattern(3))
