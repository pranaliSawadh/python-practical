def count_function(str1 , str2 , value):
	count = 0
	start = 0
	if value :
		while start < len(str1):
			start = str1.find(str2, start)  # Finds the next occurrence of str2
			if start == -1:
				break
			count += 1  # Increase the count for each occurrence
			start += 1
		return count
	elif value == False :
		if len(str2) ==1:
			for i in str1:
				if i ==str2:
					count=count+1
			return count
		elif len(str2)>1:
			while True:
				start = str1.find(str2, start)  # Finds the next occurrence of str2
				if start == -1:  # If no more occurrences are found, break the loop
					break
				count += 1  # Increment the count for each occurrence
				start += len(str2)
		return count  
		
print(count_function("sgggggggs" , "gg" , True))
print(count_function("sgggggggs" , "gg" , False))
