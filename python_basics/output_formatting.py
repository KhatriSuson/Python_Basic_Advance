name = "Hari"
age = 30
print("Name: {}, Age: {}".format(name,age))

print(f"Name:{name}, Age:{age}")

# String padding
text = "Python"
pad_text = text.center(20, "*")
print(pad_text)


# Number Formatting
price = 30.25431
print("Price: ${:.3f}".format(price))


# Formatted Table

data = [("Ram", 34), ("Hari",23), ("Sita", 22)]
print("{:<10} {:<10}".format("Name", "Age"))
for name, age in data:
    print("{:<10} {:<10}".format(name, age))
