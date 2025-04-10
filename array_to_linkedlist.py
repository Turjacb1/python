class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

def append(self,data):
    new_node=Node(data)
    if self.head is None:
        self.head=new_node
        return
    last_node = self.head
    while last_node.next:
        last_node = last_node.next
        last_node.next=new_node
    
def array_to_likded_list(arr):
    linkdelist =Linkedlist()
    for element in arr:
        linkdelist.append(element)
    return Linkedlist

arr=[1,2,3,4,5]
linkedlist = array_to_likded_list(arr)

currentnode = linkedlist.head
while currentnode:
    print(currentnode.data)
    currentnode = currentnode.next
    