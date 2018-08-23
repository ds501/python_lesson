'''
LESSON 2: Functions and Modules

'''

#############################
# PYTHON BUILT-IN FUNCTIONS

# Python 2.7 comes with 76 of its own pre-defined functions:
# https://docs.python.org/2.7/library/functions.html
#############################

max(1,5,8)



min(9, 3, -100)

abs() # causes an error (specifically, "TypeError"), as it requires exactly 1 argument:

# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: abs() takes exactly one argument (0 given)

abs(-9)



#############################
# USER-DEFINED FUNCTIONS:
# We can also define our own custom functions.
#############################

# Functions are defined in the following manner:

# def NAME( LIST OF PARAMETERS ):
#     STATEMENTS

def new_line():
    print

print "hello"
new_line()
print "world"

# Try creating a separate python program file and run it.
# command line: python Lesson_2__newLineProgram.py
# Python Console:
execfile('Lesson_2__newLineProgram.py')
# Run Console

# Exercise: define a function that prints three lines

def three_lines():
    print
    print
    print


#############################
# ARGUMENTS AND PARAMETERS IN FUNCTIONS
# To call a function you type in the function name, followed by parentheses in which you pass in arguments.
# E.g. functionName(argument1, argument2,...)
# Some functions need no arguments, others have optional arguments, still others require you to pass in arguments
# in order for the function to successfully be called.
#############################

# In the new_line() function, we did not require any arguments to pass into the function.
# We can successfully call it without arguments.

new_line()

# Other functions require arguments. Recall the abs() function which could not be called without an argument.

abs()
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: abs() takes exactly one argument (0 given)

# We can define functions that require arguments:

def print_twice(param):
    print param, param

# The print_twice() function requires 1 argument, which it then passes into a parameter called "param"
# and uses in the function.

print_twice("Yep")
# Yep Yep

# NOTE: The names of the arguments we pass into the function are totally different from the name of
# the parameters we defined within the function. It is as if param = "Yep" is
# executed when print_twice("Yep") is called. This is actually exactly what is going on. In fact,
# we can explicitly declare that param = "Yep" if we want to keep things clear:

print_twice(param="Yep")
# Yep Yep

# We can require more than one argument in a user-defined function:

def printTwoArguments(param1, param2):
    print param1, param2

printTwoArguments()
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: printTwoArguments() takes exactly 2 arguments (0 given)

printTwoArguments("Bye")
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: printTwoArguments() takes exactly 2 arguments (1 given)

printTwoArguments("Bye", "Felicia")
# Bye Felicia

# Notice what happens when we mix up our arguments by declaring them:
printTwoArguments(param2="Bye", param1="Felicia")
# Felicia Bye


#############################
# Composing Functions: putting functions within functions
#############################

# You can compose functions by calling a function within a function
print_twice(abs(-7))
# 7 7

# You can do the same by defining a function within a variable,
# and then using that variable as an argument for another function:
absolute_value = abs(7)
print_twice(absolute_value)
# 7 7


#############################
# LOCAL VARIABLES / PARAMETERS: Defining variables within functions
# When you create a local variable inside a function, it only exists in the function, you can't use it outside.
#############################

def one_plus_one():
    two = 1 + 1
    return two

two
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# NameError: name 'two' is not defined

one_plus_one()
# 2

# You may create a variable outside the function to equal the called function:

two = one_plus_one()

two
# 2


#############################
# DEFINING FUNCTIONS: THE RETURN STATEMENT
#############################

# Let's define two functions that look very similar, but one ends in a print statement,
# the other ends with a return statement.

def print_two_plus_two():
    four = 2 + 2
    print four


def return_two_plus_two():
    four = 2 + 2
    return four

# Calling the functions seem to result in the same thing:

print_two_plus_two() # 4

return_two_plus_two() # 4

# The difference is found when we attempt to define variables using the different functions

printed_variable = print_two_plus_two() # Output: 4

returned_variable = return_two_plus_two() # No output

print printed_variable # None
print returned_variable # 4

# QUESTIONS:
# How would you characterize the difference between print and return?
# When might you use a return statement?


#############################
# WORKING WITH AND IMPORTING MODULES:
# Now, let's turn to working with externally-defined functions.
# Open mainprogram.py and moduletest.py
#############################

import os
os.chdir('Lesson_2__workingFiles')

#after exercise:
os.chdir('/Users/saafid/Desktop/Teaching/Python_Lilly/Python_Lessons')



#############################
# TRACEBACKS: ERROR TRACKING
#############################

execfile("trace_back_file.py")
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#   File "trace_back_file.py", line 13, in <module>
#     cat_twice(chant1, chant2)
#   File "trace_back_file.py", line 9, in cat_twice
#     print_twice(cat)
#   File "trace_back_file.py", line 5, in print_twice
#     print cat
# NameError: global name 'cat' is not defined


# What does this "Traceback" mean?
# It's keeping track of the variables/parameters defined in each function within a program.
# When a variable or parameters is not defined, or something else goes wrong, Python traces
# the problem back through the program to the root source.

'''
A Stack Diagram: keeps track of a program's functions and variables defined within each. 
This can be used to trace back the error in a program. 
You can see that "cat" is not defined within the print_twice function, though the function
calls for it to be printed.

NOTE: We will learn about __main__ at a later time, but know that any variable defined outside of an explicit
function belongs to the __main__ function, by default. 
 

Function    |   Variables
------------------------------------------            
__main__    |   chant1 --> "Pie Jesu domine,"
                chant2 --> "Dona eis requiem."

cat_twice   |   part1 --> "Pie Jesu domine,"
                part2 --> "Dona eis requiem."
                cat --> "Pie Jesu domine, Dona eis requiem."

print_twice |   param --> "Pie Jesu domine, Dona eis requiem."

'''



################






















































