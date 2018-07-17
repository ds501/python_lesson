'''
LESSON 1: INTRO TO PYTHON LANGUAGE AND PROGRAMMING

NOTE:
    Short cut to a run line of code in the interpreter / console:  Shift + Alt + e
'''

# OUR FIRST PROGRAM
print 'Hello World'

# OUR SECOND PROGRAM
print "Hello World"

# OUR THIRD PROGRAM
print 4

# As you see, the print function works not only on string types, but also on integer and numeric types. Which brings
# us to...


'''
PYTHON DATA TYPES
'''

type("Hello, World!")
type(17)
type(3.2)
type("17")
type("3.2")

# type("Hello, World!")
# <type 'str'>
# type(17)
# <type 'int'>
# type(3.2)
# <type 'float'>
# type("17")
# <type 'str'>
# type("3.2")
# <type 'str'>


'''
VARIABLES
'''

# Assignment statements *assign* a value to a variable using = as the assignment operator:

myRapName = "Gravy D"
n = 89
rating = 2.7

print myRapName
print n
print rating

type(myRapName)
type(n)
type(rating)


# Some no-no's regarding variable names:

3Forms = "Solid, Liquid, Gas" # must begin w/ a letter
TyDolla$ign = "Or Nah?" # no illegal characters like $
raise = "the roof" # cannot use reserved keywords as variables

# There are 31 reserved keywords (see slides).


'''
STATEMENTS AND EXPRESSIONS

Basically: 
*STATEMENTS are executed.
*EXPRESSIONS are evaluated. 

'''

# print statements
print "Hi there"

#expression
"Hi there"

# assignment statement
height = 60 + 6

#expression
height

#also an expression
60 + 6

#other kinds of statements: if, while, etc.


'''
OPERATORS AND OPERANDS

+ addition
- subtraction
/ division
* multiplication
** exponentiation
() parentheses 

'''

20+32
hour-1
hour*60+minute
minute/60
5**2
(5+9)*(15-7)


# INTEGER OPERATIONS

minute = 59
minute / 60 # returns a 0


# FLOAT OPERATIONS

minute2 = 59
minute2 / 60.0 # returns 0.9833333333333333


# PEMDAS: Order of Operations

minute * 100 / 60 # returns 98


# Performing operations on strings
# The operators + and * work (to a limited extent) with strings.

"hold " + "up"

"ok " * 3


'''
INPUT
The input() and raw_input() functions allow you to interact with a user to let them define data. 
'''

n = raw_input("Please enter your name: ")
print n
n = input("Enter a numerical expression: ")
print n


'''
EXECUTE A PYTHON PROGRAM FROM SOURCE CODE
'''
# Try running the last 4 lines of code in a separate program to get a feel for running program from source code.
# Attached: Lesson_1__InputProgram.py

# There are a few ways to run a python program file. First navigate to working directory. Then do any of the following:
# * Terminal: python Lesson_1__InputProgram.py
# * Python Shell: execfile('Lesson_1__InputProgram.py')
# * Pycharm Running Console / Point and click method. Provides code completion and syntax check messages.



'''
COMPOSITION
Building something new from disparate elements. 
'''

# Compose using assignment statements:
percentage = (minute * 100) / 60

# Compose using print statements
print "The percentage is ", percentage, "%"






