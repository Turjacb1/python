#print("{:.3f} km/l".format(c))

# a,b,c,d = map(int,input().split())

#print("%0.1f"%total)

# print(f"{inn} in")


class Node:

  def __init__(self,data):
    self.data=data
    self.next=None

def createlinkedlist (arr):
    head=None
    current=None
    for data in arr:
        temp =Node(data)
        if head is None:
            head =temp
            current=temp
        else:
            current.next=temp
            current=temp
        return head
    
    def searchlinkedlist(head,value):
       index=1
       current=head
       while current:
          if current.data ==value:
             return index
          index=index+1
          current=current.next
          return -1
       
       if __name__=="__main__":
          a=[5,10,15,20,100]
          head=createlinkedlist(a)
          print("index ",searchlinkedlist(head,100))
             





   

   
  




