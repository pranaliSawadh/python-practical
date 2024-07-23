#string datatype
str = "hello world"
print(str[1])
print(str[6:10])
print(str[5:])
print(str[-1])


 #list
 
list =[10,-20,15.5,"vijay","mary"]
print(list)
print(list[1:3])
print(list[-1])
print(list * 2)

#tuple
tpl=(10,20,30,"vijay" , "mary")
print(tpl)
print(tpl[1:3])
print(list[-2])
print(list * 2)
# tpl[0] =100   will give you an error

#range
r=range(10)
print(r)
r=range(30,40,2)	#this will print in a differnce of 2 between 30 to 40
for i in r:
 print(i)

#bytes datatype
element = [10,2,30,4,50,6,70,8,90,10]
x=bytes(element)
for num in x:
 print(num)
 
