# String
print("Hello, World")


# Multi values separated by a custom separator 

print("ValueOne", "ValueTwo", "ValueThree", "ValueFour", sep=' | ')


# Result of an expression

a = 34
b = 45
print("The sum of = ", a + b)


# Without a newline character 

print("This will not end with a new line.", end=' ')


# Redirecting output to a file 

with open('Output.txt', 'w') as f:
    print("Written to the file." , file=f)



# Flush the output immediately
# Flush parameter is an optional argument that can be used with certain output functions, such as the 'print()' function and file I/O operations, to control whether the output is immediately written to the underlying output stream or buffered and written later.

# When 'flush' is set to 'True', it forces the output to be immediately written to the output stream, bypassing any buffering.

# When 'flush' is set to 'False', (the default), or if you omit the 'flush' parameter, the output may be buffered, which means it is sotred in memory temporarily.


# Simple Example:-
# print("Flush the value.", flush=True)

# Without flush=True (default behaviour)

with open('flush.txt', 'w') as f:
    for i in range(5):
        print(f"Line {i}")



# With flush=True

with open('flush_true.txt', 'w') as f:
    for i in range(5):
        print(f"Line {i}", flush=True)
