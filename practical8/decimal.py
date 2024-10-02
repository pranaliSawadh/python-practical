


def str_to_int(string):
		decimal_dict = {"0":0 , "1":1 , "2":2 , "3":3 , "4":4 , "5":5 ,"6":6 , "7":7 , "8":8 , "9":9 }
		digit_dict = {0:"0" , 1:"1" , 2:"2" , 3:"3" , 4:"4" , 5:"5" , 6:"6" , 7:"7" , 8:"8" , 9:"9" }
		number = ""
		l = list(digit_dict.keys())
		for value in sorted(digit_dict.keys()):
			if len(string)==0:
				return 0
			elif len(string)==1:
				if string == digit_dict[value]:
					#print(type(value))
					return value
			else:
				return decimal_dict[string[0]]*pow(10,len(string)-1)+str_to_int(string[1:])
print(str_to_int("1"))
print(str_to_int("100"))
print(str_to_int("12345"))
