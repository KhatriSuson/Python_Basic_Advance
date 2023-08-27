from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)
front_item = queue.popleft()

queue.pop()
print("After pop operation",queue)
