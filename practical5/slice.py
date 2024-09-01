def slice(s,start,end,step):
	if(step==0):
		print("Step can't be Zero")
		return s
	elif(start>=end):
		return ''
	res=[]
	while(start<end-1):
		res.append(s[start])
		start+=step
	print(res)
	return res
s=[1,2,3,4,5,6,7,8,9]
#l=[1,6,1]
slice(s,1,7,2)
