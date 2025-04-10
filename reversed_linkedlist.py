class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_linked_list(arr):
    head = None
    temp = None
    for data in arr:
        temp = Node(data)  # Create a new node
        if head is None:
            head = temp
        else:
            temp.next = head  # Prepend the new node to the beginning
            head = temp
    return head

def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev  # The new head after reversal

# Example usage
arr = [5, 10, 30]
head = create_linked_list(arr)

print("Original list:")
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("NULL")

head = reverse_linked_list(head)

print("\nReversed list:")
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("NULL")
