''' USE THIS AS AN EXAMPLE OF TRACEBACKS'''

def print_twice(param):
    print param, param
    print cat ## THIS FUNCTION DOESN'T KNOW WHAT "cat" IS

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

chant1 = "Pie Jesu domine, "
chant2 = "Dona eis requim."
cat_twice(chant1, chant2)