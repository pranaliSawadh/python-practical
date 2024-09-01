def rom(text , text_base):
	num = int(text , text_base)
	#1==>"I" , 4==>"IV" , 9==>"IX" , 10==>"X" , 40 ==>"XL" , 50 ==> "L" , 90 ==>"XC" , 100 ==>"C" , 400 ==>"CD" , 500==>"D" , 900 ==>"CM" , 1000 ==> "M"
	roman = {1:"I",4:"IV",5:"V" , 9:"IX",10:"X", 40:"XL", 50:"L", 90:"XC",100:"C", 400:"CD",500:"D", 900: "CM", 1000:"M"}
	roman_number = ""
	for value in sorted(roman.keys(),reverse=True):
		while num>= value:
			roman_number += roman[value]
			num = num-value
	return roman_number
print(rom("10",10))
print(rom("10",8))
print(rom("1F",16))
print(rom("10",2))
