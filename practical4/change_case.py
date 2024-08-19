def change_case(text,style):
	#to check for the correct style input
	if style in ["C" , "c" , "S" , "s" , "Z" , "z" , "R" ,"r"]:
		if style in ["S" ,"s"]:
			return small_case(text)
		elif style in ["C" ,"c"]:
			return capital_case(text)
		elif style in ["R" ,"r"]:
			return reverse_case(text)
		elif style in ["Z" ,"z"]:
			return zigzag_case(text)
	else:
		return "The style you've entered is incorrect please select one of the following:\n 'C' or 'c' for caapital or upper case \n 's' or 'S' for small or lower case \n 'r' or 'R' for reverse case \n 'z' or 'Z' for zigzag case"
	#to capitalize the text 
def capital_case(text):
		n = ""
		for i in text:
			if ord(i)>=97 and ord(i)<=122:
				num = ord(i)-32
				n = n+chr(num)
			elif ord(i)>=65 and ord(i)<=90:
			 		n = n+i
		return n
		
	#to change case to small for all
def small_case(text):
		n = ""
		for i in text:
			if ord(i)>=65 and ord(i)<=90:
				num = ord(i)+32
				n = chr(num) + n
			elif ord(i)>=97 and ord(i)<=122:
		 		n = n+i
		return n
	
def reverse_case(text):
		n = ""
		for i in text:
			if ord(i)>=97 and ord(i)<=122:
				num = ord(i)-32
						#n = n+chr(num)
			elif ord(i)>=65 and ord(i)<=90:
				num = ord(i)+32
			n=n+chr(num)
		return n	
			
def zigzag_case(text):
    n = ""
    first = 'A' <= text[0] <= 'Z'
    for i in range(len(text)):
        if i % 2 == 0:  			 # Even index
            if first:  				 # First char is uppercase
                if 'a' <= text[i] <= 'z': 	 # Lowercase to uppercase
                    n += chr(ord(text[i]) - 32)
                else:
                    n += text[i]
            else:  				 # First char is lowercase
                if 'A' <= text[i] <= 'Z': 	 # Uppercase to lowercase
                    n += chr(ord(text[i]) + 32)
                else:
                    n += text[i]
        else:  					# Odd index
            if first:  				# First char is uppercase
                if 'A' <= text[i] <= 'Z':       # Uppercase to lowercase
                    n += chr(ord(text[i]) + 32)
                else:
                    n += text[i]
            else:  				# First character is lowercase
                if 'a' <= text[i] <= 'z':  	# Lowercase to uppercase
                    n += chr(ord(text[i]) - 32)
                else:
                    n += text[i]

    return n

print(change_case("Pranali","C"))
print(change_case("sawadh","c"))
print(change_case("Pranali","s"))
print(change_case("Sawadh","S"))
print(change_case("Pranali","Z"))
print(change_case("pranali","z"))
print(change_case("pranALI","R"))
print(change_case("SAWadh","r"))
print(change_case("pranaLI","w"))
