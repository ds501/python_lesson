'''
For Lesson 2: Examples of importing modules and packages.

'''

##########################
# IMPORTING MODULES
##########################
import os
os.chdir('Lesson_2__workingFiles')
sys.path.append(os.getcwd())


import moduletest

print ageofqueen
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# NameError: name 'ageofqueen' is not defined

print moduletest.ageofqueen
# 78

printhello()
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# NameError: name 'printhello' is not defined

moduletest.printhello()
# hello


Piano.printdetails()
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# NameError: name 'Piano' is not defined

moduletest.Piano.printdetails()
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: unbound method printdetails() must be called with Piano instance as first argument (got nothing instead)

moduletest.Piano().printdetails()
# What type of piano? >? grand
# What height (in feet)? >? 5
# How much did it cost? >? 2500
# How old is it (in years)? >? 8
# This piano is a/an 5 foot grand piano, 8 years old and costing 2500 dollars.

#A more typical way of handling the above function call:
cfcpiano = moduletest.Piano()
cfcpiano.printdetails()


##########################
# ASSIGNING ITEMS TO A LOCAL NAME
##########################

timesfour = moduletest.timesfour

# Using the local name
print timesfour(565)


##########################
##########################
# IMPORT ITEMS DIRECTLY INTO YOUR PROGRAM:
# Use "from moduleName import variable, function, or class"
##########################

# import variable from external module
from moduletest import ageofqueen

# import function from external module (same language)
from moduletest import printhello

# now try using them. They are now defined locally. No need to reference the module name as prefix.

print ageofqueen
printhello()

# Importing all items from a module is slightly different, can be dangerous.

print numberone
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# NameError: name 'numberone' is not defined

numberone = "We're number one!!!"

print numberone
# We're number one!!!

# Now let's see what happens when we import all (*) from moduletest (which has its own defined numberone variable)
from moduletest import *

print numberone
# 1
# importing * overwrote our locally defined variable. Use the "from __ import *" statement cautiously.