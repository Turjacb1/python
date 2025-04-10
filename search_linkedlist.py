class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_linked_list(arr):
    head = None
    current = None
    for data in arr:
        temp = Node(data)
        if head is None:
            head = temp
            current = temp
        else:
            current.next = temp
            current = temp
    return head

def search_linked_list(head, value):
    index = 1
    current = head
    while current:
        if current.data == value:
            return index
        index += 1
        current = current.next
    return -1

if __name__ == "__main__":
    a = [5, 10, 30, 60, 100]
    head = create_linked_list(a)
    print("Index:", search_linked_list(head, 100))
