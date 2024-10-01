def count_palindrome(text):
	count = 0
	for i in text:
		if isinstance(i,str) or isinstance(i,int):	#check if object is string or integer
			count += ispalindrome(str(i)) and len(str(i))%6==3
	return count
def ispalindrome(text):
	return text == text[::-1]
print(count_palindrome(["sgggggggs","racecarar","abccbaabcbaabccba",121,"1001",123111321,23432]))
