Example 1:
	
# in this example, I decided to use music notation

>>> def print_musicnotes():
	print("Do, Re, Mi")
  
# Explanation: In this Example, def print_musicnotes(): and the parameter is print("Do, Re, Mi"). 
# When called, the function displays the following argument

>>> print_musicnotes()
Do, Re, Mi

Example 2
# I am a big fan of aviation and aerospace, so i tried to calculate the speed of sound using a mach 1 value of 768 MPH
# In this example, values are expressed as follows. Arguments are the 768, 1536 and 2302

>>> def print_mach1():
	print("768")
	
>>> def print_mach2():
	print("1536")

>>> def print_mach3():
	print("2302")

# When the values are called, the output is as follows

>>> print_mach1()
768
>>> print_mach2()
1536
>>> print_mach3()
2302
>>> 

# in this example, the parameters are expressed using variables. The arguments are x1*1,x1*2 and x1*3
	
>>> def print_x1():
	print("x1*1")

	
>>> def print_x2():
	print("x1*2")

	
>>> def print_x3():
	print("x1*3")

# when called, the output results in the following variables
	
>>> print_x3()
x1*3
>>> print_x2()
x1*2
>>> print_x1()
x1*1
>>> 

# using the same sample, but in expression format results in the following output. 
# the arguments are 768*1, 768*2 and 768*3

>>> mach1=768*1
>>> mach2=768*2
>>> mach3=768*3

# When called, results are as follows

>>> print(mach3)
2304
>>> print(mach2)
1536
>>> print(mach1)
768
>>> 
EXAMPLE 3
# in the first part of the example, I used a local variables (inside the function) and was able to get a response from python
>>> x=5
>>> y=10
>>> print(x+y)
15

# in the second part of the example, I used a local varible outside the function and received an error message. See results below
>>> print(x)+y
5
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    print(x)+y
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
>>> 

Example 4
# for this example, I assigned my name as the parameter as unique_name

>>> def unique_name():
	print("Misael")

	
>>> unique_name()
Misael
>>>

if I try to print the parameter outside of the function in the next line, I get a syntax error

>>> Misael
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    Misael
NameError: name 'Misael' is not defined
>>> 

Example 5
# in this particular example, the variable is outside the function 
# when the program runs, the outside variable is executed separately because they are the same

>>> x = "awesome"
>>> def myfunc():
	x = "fantastic"
	print("Python is " + x)
	
>>> print("Python is " + x)
Python is awesome
