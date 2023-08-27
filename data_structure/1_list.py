# Creating a list

list = [1, 2, 3, 4, 5]

# Accessing elements of list
print(list[0])
print(list[4])


# Modify Element
list[2] = 10
print("Modify list = ", list)

list.append(6)
print("After append the list = ", list)

list.remove(1)
print("After remove = ", list)

list.remove(list[0])
print("Remove element according to arrat index of list= ", list)
