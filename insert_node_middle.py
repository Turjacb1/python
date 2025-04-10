class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def create_linked_list(arr):
  head = None
  current = None
  for data in arr:
    new_node = Node(data)
    if head is None:
      head = current = new_node
    else:
      current.next = new_node
      current = new_node
  return head

def print_list(head):
  temp = head
  while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
  print("NULL")

def insert_middle(head, position, value):
  if position < 0:
    print("Invalid position")
    return

  temp = head
  counter = 0
  while temp and counter < position:
    counter += 1
    temp = temp.next

  if not temp:
    print("Invalid position")
    return

  new_node = Node(value)
  new_node.next = temp.next
  temp.next = new_node

# Main program
arr = [5, 10, 30, 50]
head = create_linked_list(arr)

print("Original list:")
print_list(head)

insert_middle(head, 1, 500)

print("List after insertion:")
print_list(head)
