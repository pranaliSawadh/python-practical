#function to implement dfa acception string ends with b 
def dfa_implementation(text):
	#final state occur only when it comes to q1 state
	final_state = {"q1"}   
	result = q0(text)
	#if we reach the final state
	if result in final_state:
		return "accepted"
	else:
		return "rejected"
		
#q0 state where "a" goes to q0 and "b" goes to q1 state 
def q0(text):
		alphabets = {"a","b"}
		if len(text)>0:
			symbol = text[0]
			if symbol in alphabets:
				if symbol == "b" :
					return q1(text[1:])
				else:
					return q0(text[1:])
			else:
				return "rejected"
		else:
			return "q0"
			
#q1 state where "a" goes to q0 and "b" goes to q1 state  
def q1(text):
		alphabets = {"a","b"}
		if len(text)>0:
			symbol = text[0]
			if symbol in alphabets:
				if symbol == "b" :
					return q1(text[1:])
				else:
					return q0(text[1:])
			else:
				return "rejected"
		else:
			return "q1"

print(dfa_implementation("abababab"))	
print(dfa_implementation("ababa"))	
