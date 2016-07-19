#########
#  Melissa Skills:Functions
#  Gryffindor
#########

"""Skills Assessment: Functions
	done Write a function that does not take any arguments and prints <Hello World>.
	done Write a function that takes a name as a string and prints <Hi> followed by the name.
	done Write a function that takes two integers and multiplies them together. 
		 Print the result inside of the function.
	done Write a function that takes a string and an integer and prints that string that many times. 
		 For example, if you passed in <hello> and 5, it should print hellohellohellohellohello.
	done Write a function that takes an integer and prints <Higher than 0> 
		 if higher than zero and <Lower than 0> if lower than zero. 
		 If integer is 0 print <Zero>.
	done Write a function that takes an integer and returns a boolean (True or False), 
		 depending on whether the number is evenly divisible by 3.

	done Write a function that takes a sentence as one string and returns the number of spaces.

"""


def HelloWorld():
    """Function that does not take any arguments and prints 

        Hello World

    """
    #print hello world
    print("Hello World")
    
    return


def print_Name(name):
	"""Write a function that takes a name as a string and prints <Hi>
		followed by the name.
	"""
	#print Hi and the name argument
	print("Hi " + name)

	return 

def mult_twoNums(num1, num2):
	"""	Write a function that takes two integers and multiplies them together. 
		Print the result inside of the function.

	"""
	#multiply two arguments sent in and display result
	result=num1*num2
	print("The result of {} * {} = {}".format(num1, num2, result))

	return

def repeat_String(myString,n):
	"""Write a function that takes a string and an integer and prints that string 
		that many times. 
		For example, if you passed in <hello> and 5, 
		it should print hellohellohellohellohello.
		repeat_String(myString, n)
		"""
	#print the string the number of times indicated by the function argument n
	print (myString*n)

def evaluate_Number(num):
	"""Write a function that takes an integer and prints 
		
		If higher than zero
			<Higher than 0> 

		If lower than zero. 
			<Lower than 0> 
		
		If integer is 0 print 
			<Zero>.
	"""
	#evaluate the function argument num and drop into the appropriate 
	#print funcation
	if num>0:
		print("Higher than 0")
	elif num<0:
		print("Lower than 0")
	elif num == 0:
		print("Zero")

	return


def divide_By_3(num):
	"""Write a function that takes an integer and returns a boolean 
		(True or False), 
		depending on whether the number is evenly divisible by 3.
	"""

	#Modal the function argument num to find a remainder.  
	#if there is a remainder the number was not divisible by 3 -> return false
	#if there is no remainder the number was divisiable by 3 -> return true
	if (num%3)==0:
		return(True)
	
	elif(num%3)!=0:
		return(False)


def Count_whiteSpace(mySentence):
	"""Write a function that takes a sentence as one string and returns the number of spaces.
		Example: 'My fellow Americans' = 3
	"""

	spaces = 0
	for item in range(0,len(mySentence)-1):
	
		#look for matching spaces
		if mySentence[item] == " ":
			#increment the counter
			spaces+=1

	return(spaces)

def Tip_Me(meal, tip="15"):
	"""Write a function that can be passed a meal price and a tip percentage. 
	It should return the total amount paid 
	(price + price * tip). 
	However: passing in the tip percentage should be optional; 
	if not given, it should default to 15%.

	result = meal + (meal*tip)

	"""
	#turn the tip into a decimal and yes I know it could have been done in a single math
	#equation but I don't think it's very clean code to do it.  Sorry
	tip = (float(tip)/100)
	
	#Complete the tabulation
	result = meal + (meal*tip)
	
	#format the output
	result = ('{0:.2f}'.format(result)) 
	
	#send it back
	return( result )

def Even_and_Odd(num):
	"""Write a function to deduce whether a number is even or odd and positive or negative 
		returnt the two values and print them out as sign and parity

	"""
	#check by using modal
	#if num is even set the elem=Even; if the num is odd set the elem=odd
	if num%2 == 0:
		elem1='Even'
	elif num%2!=0:
		elem1='Odd'

	#check by using modal
	#if num is even set the elem=Even; if the num is odd set the elem=odd
	if num < 0:
		elem2 = 'Negative'
	elif num > 0:
		elem2 = 'Positive'

	return(elem1, elem2)

def state_Sales_Tax(price, default_tax=.05, state='default'):
	"""refactor the code: example 1
	
	Your function will pass in the default tax amount (5%), 
	a state abbreviaton, and the default tax amount as parameters.
	"""

	if state == "CA":
		total =  price + (.07 * price)
		total = ('{0:.2f}'.format(total))
	
	elif state != "CA":
		total = price + (default_tax * price)
		total = ('{0:.2f}'.format(total))
	
	return(total)

def call_the_Engineer(sender,name,job_title='Engineer'):
	"""Turn the below block of code into a function. 
	Take a name and a job title as parameters, 
	making it so the job title defaults to <Engineer> if a job title is not passed in.
	And then:
	now call the function again and return items
	to a value called reciever
	Use that variable to construct your letter
	"""

	#if the job_title comes in blank use the default to construct the string
	if job_title == "":
	    print job_title + " " + name
	
	#if the job_title was not empty use the argument to construct the string
	elif job_title !="":
	    print job_title +" " + name


	#send back all the items so we can construct the message in the second 
	#iteration of this function call.   Look we did two things with one function... WooHooo
	return(sender, name, job_title)

def append_me_some_numbers(num):
	"""This function will take a number and append it to list of numbers
	"""
	#intialize your list preset values
	numbers = [1,2]

	#append in the value we got as an arguement from the function
	numbers.append(num)

	print(numbers)

	#it's not good form to return nothing.........
	return

#######################################################################################################
# End of Function definitions
#######################################################################################################








#######################################################################################################
# Beginning of testing
#######################################################################################################

print("Function: HelloWorld")
HelloWorld()
print("***********************************************************\n")

print("Function: print_Name(name)")
print_Name("Ally")
print("***********************************************************\n")

print("Function: mult_twoNums(num1,num2)")
mult_twoNums(2,3)
print("***********************************************************\n")

print("Function: repeat_String(myString)")
repeat_String("Ally",10)
print("***********************************************************\n")

print("Function: evaluate_Number: 3")
evaluate_Number(3)
print("***********************************************************\n")

print("Function: evaluate_Number: -9")
evaluate_Number(-9)
print("***********************************************************\n")

print("Function: evaluate_Number: 0")
evaluate_Number(0)
print("***********************************************************\n")

print("Function: divide_By_3: 9")
print(divide_By_3(9))
print("***********************************************************\n")

print("Function: divide_By_3: 10")
print(divide_By_3(10))
print("***********************************************************\n")

print("Function: Count_whiteSpace(myString)")
print(Count_whiteSpace("Well hello Ally!  I hope you are having a great night."))
print("***********************************************************\n")

print("Function: Tip_Me(meal,tip)")
result =Tip_Me(20,10)
print "My meal cost $20 and I tipped 10%.  Total Meal Cost ${} ".format(result)
print("***********************************************************\n")

print("Function: Tip_Me(meal,tip)")
result =Tip_Me(20, )
print "My meal cost $20 and I tipped default <15>%.  Total Meal Cost ${} ".format(result)
print("***********************************************************\n")


print("Function: Even_and_Odd(num)")
num = -6
result =list(Even_and_Odd(num))
parity = result[0]
sign = result[1]
print ( ("The results of our test indicate that the parity of {} is {} and the sign is {}".format(num,parity, sign)) )
print("***********************************************************\n")


print("Function: Even_and_Odd(num)")
num = -13
result =list(Even_and_Odd(num))
parity = result[0]
sign = result[1]
print ( ("The results of our test indicate that the parity of {} is {} and the sign is {}".format(num,parity, sign)) )
print("***********************************************************\n")


print("Function: Even_and_Odd(num)")
num = 45
result =list(Even_and_Odd(num))
parity = result[0]
sign = result[1]
print ( ("The results of our test indicate that the parity of {} is {} and the sign is {}".format(num,parity, sign)) )
print("***********************************************************\n")


print("Function: Even_and_Odd(num)")
num = 100
result =list(Even_and_Odd(num))
parity = result[0]
sign = result[1]
print ( ("The results of our test indicate that the parity of {} is {} and the sign is {}".format(num,parity, sign)) )
print("***********************************************************\n")

print("Function: state_Sales_Tax(price, default_tax=.05, state='default')")
print (state_Sales_Tax(20.0, state='CA'))
print("***********************************************************\n")

print("Function: state_Sales_Tax(price, default_tax=.05, state='default')")
print (state_Sales_Tax(20.0))
print("***********************************************************\n")


print("Function: call_the_Engineer(sender,name, job_title='Engineer')")
call_the_Engineer('None',name='Jane Hacker')
print("***********************************************************\n")

user_name = "Jane Blackhat"
print("Function: call_the_Engineer(sender,name, job_title='Engineer')")
call_the_Engineer('None',user_name, job_title='CTO')
print("***********************************************************\n")


user_name = "Ally Blackhat"
sender_name="Melissa"
print("Function: call_the_Engineer(sender, name, job_title='Engineer')")
reciever = call_the_Engineer(sender_name, user_name, job_title='Awesome Advisor')
print( "Dear {} {}, I think you are amazing!\nSincerely,\n{}".format(reciever[2], reciever[1], reciever[0]))
print("***********************************************************\n")


print("Function: append_me_some_numbers(4)")
append_me_some_numbers(4)
print("***********************************************************\n")

print("Function: append_me_some_numbers(122)")
append_me_some_numbers(122)
print("***********************************************************\n")

print("Function: append_me_some_numbers(-19)")
append_me_some_numbers(-19)
print("***********************************************************\n")

