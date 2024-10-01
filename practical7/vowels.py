def count_text(L):
	count_of_text = []
	vowels = "aeiou"
	for obj in L:
		if isinstance(obj,str):		#check if obj is string
			temp_vowels = []	
			for i in obj:
				if i in vowels:
					temp_vowels.append(i)
			count_of_vowels = []
			for char in temp_vowels:
				count_of_vowels.append(temp_vowels.count(char))
				total_count =0
				for counts in count_of_vowels:
					if counts ==1:
					 	total_count+=1
					if total_count==len(count_of_vowels):
					 	count_of_text.append(obj)
		else:
			return "entered object is not a string"
	return len(count_of_text)
print(count_text(["abca","abcabc","abcde","aabbccee","aouaouaou"])) 
