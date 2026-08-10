#variable declaration 
a , b = int (input('enter the first number :')) , int (input('\n enter the second number :'))
print (' a: ',a , '\n b: ',b)

#arithmetic
print ("a + b :" , a+b)
print ("a - b :" , a-b)
print ("a x b :" , a*b)
print ("a / b :" , a / b)
print ("a '%' b :" , a % b)
print ("a // b :" , a //b)

#comparison 
print ('is a>b ?', a > b)
print ('is a<b ?', a < b)
print ('is a=b ?', a==b ) 

# combined condition 

numbers = [1,2,3,4,5,6,7,8,9,10]

print (numbers)
print (' is 2 and 7 in numbers ?\n',  2 in numbers and 7 in numbers)
print (' is 3 or 11 in numbers ?\n',  3 in numbers or 11 in numbers)
print (' is  9 not in numbers ?\n',  9 not in numbers)

# loop incrementation 
makes = 0
for i in range (1,10): 
 makes += 1
 print (f'make {makes}') 