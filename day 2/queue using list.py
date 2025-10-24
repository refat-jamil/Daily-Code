# A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.

queue = []

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
print(queue)

dequeue = queue.pop(0)
print(dequeue)
print(queue)


dequeue = queue.pop(0)
print(dequeue)
print(queue)