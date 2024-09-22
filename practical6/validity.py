#function to check valid text in the given language or not
def check_validity(text):
		pairs = {'(':')','{':'}','<':'>','[':']'}
		symbols = ['(',')','[',']','{','}','<','>']
		stack = []	#initialize empty stack
		for symbol in text :
			if symbol in symbols:
				if symbol in pairs:			#checks if symbol is opening symbol 
					stack.append(symbol)		#push opening symbol to the stack
				elif symbol in pairs.values():		#checks if symbol is closing symbol
					if stack ==[]:
						return "invalid string : no opening symbol to match closing symbol"
					stack_top = stack.pop()		#access topmost element of stack
					if pairs[stack_top] !=symbol:
						return "invalid string :last opening symbol do not matches the closing symbol"
			else:
				return "invalid string : Invalid character"
		if stack == []:		#if stack is empty means every open symbol has its closing symbol
			return "valid string"
		else:
			return "invalid string : no closing symbol found for last opening symbol"
			
#function to print number of valid and invalid strings in given list
def get_valid_invalid_text_count(texts_list):
   valid_count = 0
   invalid_count = 0
   list_of_valid = []
   for i in texts_list:
   	if isinstance(i,str):		#checks if i is string or not
   		list_of_valid.append(check_validity(i))		
   for j in list_of_valid:
   			if j.startswith("valid"):
   				valid_count+=1
   			else:
   				invalid_count+=1
   return (valid_count,invalid_count)
   
#input for function check_validity(text)
list_of_string = ["{12,2}","{}{[]}","({[})","{{{}","(<>)","(<)>"]
for string in list_of_string:
	print(check_validity(string))
	
#input for function get_valid_invalid_text_count(text_list)
print(get_valid_invalid_text_count(["[]{()}",[1,2,3],{1234,12,1} , "{{[}}" , (1)]))

