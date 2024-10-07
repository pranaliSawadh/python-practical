import time
#function to find factorial of a number with if else (approach 1)
def factorial1(num):
	if num<0:
		return "Error"
	if num<2:
		return 1
	else:
		fact = 1
		for i in range(2,num+1):
			fact*=i
	return fact

#function to find factorial of a number with if else alternating condition(approach 2)
def factorial2(num):
	if num<0:
		return "Error"
	if num>2:
		fact = 1
		for i in range(2,num+1):
			fact*=i
		return fact
	else:
		return 1

#function to find factorial of all odd numbers till 1000(approach 1)
def f1():
	for i in range(1,1000,2):
		x =factorial1(i)
	
#function to find factorial of all odd numbers till 1000(approach 2)
def f2():
	for i in range(1,1000,2):
		x =factorial2(i)

#check performance of both approaches
def check_performance(approaches):
	total_time_taken = []
	for approach in approaches:
		for i in range(100):
			start_time = time.time()
			approach()
			end_time = time.time()
			time_taken =[]
			time_taken.append(end_time - start_time)
		total_time_taken.append(sum(time_taken)/100)	#taking average of time taken by each approach
	return total_time_taken
	
print(check_performance([f1,f2]))
print(check_performance([f2,f1]))
