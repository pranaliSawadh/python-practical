#function to get second smallest and second largest integer in given list
def get_second_smallest_second_largest(L):
	integers = []		#list of integers from all datatype
	for obj in L:
		integers.extend(numeric_values(obj))
	
	return second_smallest(integers),second_largest(integers)
	
#function to get second smallest number of all integer without using any builtin functions   
def second_smallest(integers):
	smallest ,second_smallest = None,None
	for number in integers:
		if smallest is None:
			smallest = number
		elif number<smallest:
			second_smallest = smallest
			smallest = number
		elif (second_smallest is None or number<second_smallest) and smallest != number:
			second_smallest = number
	return second_smallest
	
#function to get second largest number of all integer without using any builtin functions   
def second_largest(integers):
	largest,second_largest=None,None
	for number in integers:
		if largest is None:
			largest=number
		elif number > largest:
			second_largest = largest
			largest = number
		elif  (second_largest is None or number>second_largest) and number !=largest:
			second_largest = number	
	return second_largest

#function to get valid number of integer from given list of mixed datatype   
def numeric_values(obj):
		numeric = []
		if isinstance(obj,(int,float)):
			numeric.append(obj)
		elif isinstance(obj,dict):
			for key,value in obj.items():
				numeric.extend(numeric_values(key))
				numeric.extend(numeric_values(value))
		elif isinstance(obj,(list,tuple,set)):
			for value in obj:
				numeric.extend(numeric_values(value))
		return numeric
		
L = ["SG",("A"),5,{'a':45 , (4,7):54},[None,5]]
print(get_second_smallest_second_largest(L))
