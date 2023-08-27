stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print(stack)

top_item = stack.pop()



# class Stack:

#     def __inti__(self):
#         self.items = []

#     def is_empty(self):
#         return len(self.items) == 0

#     def push(self, item):
#         self.items.append(item)


#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
        
#         else:
#             raise IndexError("pop from empty stack")


#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]

#         else:
#             raise IndexError("Peek from empty stack")


#     def size(self):
#         return len(self.items)


# stack = Stack()

# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.push(5)

# print("Stack size:", stack.size())
# print("stack peek", stack.peek())

# while not stack.is_empty():
#     print("Popped:", stack.pop())


# print("hello")


