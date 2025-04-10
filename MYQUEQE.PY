class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)  # Add item to the end of the list

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Remove and return the first item in the list
        else:
            print("Queue is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Example usage:
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Queue:", q.items)  # Output: [1, 2, 3]

print("Dequeue:", q.dequeue())  # Output: 1
print("Queue:", q.items)  # Output: [2, 3]

q.enqueue(4)
print("Queue:", q.items)  # Output: [2, 3, 4]