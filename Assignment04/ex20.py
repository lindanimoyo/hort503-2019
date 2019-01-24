from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1

#current_line += 1
#Addition assignment
#+= is an assignment operator, that, when followed by an expression with a
#numerical value, will add the value of that expression to the value of the
#variable to the left of the operator, and assign the result to that variable.

print_a_line(current_line, current_file)

current_line += 1

print_a_line(current_line, current_file)

current_line += 1

print_a_line(current_line, current_file)
