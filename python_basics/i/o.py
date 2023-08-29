# input = input("Enter your name ")
# print("hello,  "  + input +  "!")


name = "Ram"
age = 30
print("Name:", name)
print("Age:", age)


# Arithmetic Calculation

# n1 = float(input("Enter First Number:"))
# n2 = float(input("Enter second Number:"))
# sum = n1 + n2
# print("The sum of two number is = ", sum)



# Formatted Output
price = 200
quantity = 5
total = price * quantity

print(f"Total cost for {quantity} items: ${total:.2f}")



# Reading and Writing to files

with open("test.txt", "w") as file:
    file.write("Hello, this is a file !\n")
    file.write("Python programming is awesome!")


with open("test.txt", "r") as file:
    contents = file.read()
    print(contents)