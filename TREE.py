class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, level=0):
        
        print(" " * level * 4, self.data)  # Indentation for better visualization
        for child in self.children:
            child.print_tree(level + 1)  # Recursive call with increased level

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("mac"))
    laptop.add_child(TreeNode("surface"))
    laptop.add_child(TreeNode("thinkpad"))

    cellphone = TreeNode("Cellphone")  # Corrected typo
    cellphone.add_child(TreeNode("iphone"))
    cellphone.add_child(TreeNode("Google Pixel"))  # Corrected capitalization
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("Tv")
    tv.add_child(TreeNode("samsung"))
    tv.add_child(TreeNode("Lg"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root

if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
