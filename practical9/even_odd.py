import time

def get_even_odd_count1(L):
	even,odd = 0,0
	for i in L:
		if i%2==0:
			even+=1
		elif i%2==1:
			odd+=1
	return even,odd


def get_even_odd_count2(L):
	even,odd = 0,0
	for i in L:
		even+=(1-i%2)
		odd+= i%2
	return even,odd


def get_even_odd_count3(L):
	even,odd = 0,0
	for i in L:
		if i%2:
			odd+=1
		else:
			even+=1
	return even,odd

	
def get_even_odd_count4(L):
	even,odd = 0,0
	for i in L:
		if int(bin(i)[-1])==0:
			even+=1
		else:
			odd+=1
	return even,odd

	
def check_performance(approaches):
	sample1 = [1,2,3,4,5,6,7,8,9,10]
	avg_time_taken = []
	for approach in approaches:
		for i in range(10):
			start_time = time.time()
			approach(sample1)
			end_time = time.time()
			time_taken =[]
			time_taken.append(end_time - start_time)
		avg_time_taken.append(sum(time_taken)/10)	#taking average of time taken by each approach
	min_time = min(avg_time_taken)
    
    # Calculate percentage relative to the fastest approach
	percent_performance = [(time / min_time) * 100 for time in avg_time_taken]
	return percent_performance
	#return avg_time_taken

print(check_performance([get_even_odd_count1 , get_even_odd_count2, get_even_odd_count3 , get_even_odd_count4]))
