class BinarysearchTreenode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            # Handle duplicate data here (optional)
            # You could raise an exception or ignore duplicates
            pass
        elif data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarysearchTreenode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarysearchTreenode(data)

    def in_order_traversal(self):
        element = []
        if self.left:
            element += self.left.in_order_traversal()
        element.append(self.data)
        if self.right:
            element += self.right.in_order_traversal()
        return element

def build_tree(elements):  # Use plural for clarity
    root = BinarysearchTreenode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
