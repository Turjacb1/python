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
            temp.next = head  # Prepend for insertion at beginning
            head = temp
    return head

def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head  # Link the new node to the existing list
    return new_node  # Return the new head

def print_list(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("NULL")

# Example usage
arr = [5, 10, 30]
head = create_linked_list(arr)

print("Original list:")
print_list(head)

head = insert_at_beginning(head, 500)  # Insert 500 at the beginning

print("\nList after insertion:")
print_list(head)
